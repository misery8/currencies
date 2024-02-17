import logging
from dateutil.parser import isoparse

from django.db import transaction
import requests
from requests.exceptions import (
    Timeout,
    RequestException
)
from celery import shared_task

from .models import Currency

logger = logging.getLogger(__name__)


@transaction.atomic
@shared_task
def load_currencies():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Timeout:
        logger.error('Timeout occurred while loading currencies data')
    except RequestException as e:
        logger.error(f'Request exception occurred: {e}')
    except Exception as e:
        logger.error(f'Unexpected error occurred: {e}')
    else:
        data = response.json()
        date = isoparse(data['Date']).strftime('%Y-%m-%d')

        for charcode, info in data['Valute'].items():
            try:
                currency, exist = Currency.objects.get_or_create(
                    charcode=charcode,
                    date=date,
                    defaults={
                        'charcode': charcode,
                        'date': date,
                        'rate': info['Value']
                    })
                currency.save()
            except Exception as e:
                logger.error(f'Error occurred while processing currency {charcode}: {e}')
