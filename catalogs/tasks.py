import logging

import requests
from requests.exceptions import (
    Timeout,
    RequestException
)
from celery import shared_task

from .models import Currency

logger = logging.getLogger(__name__)


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

        for charcode, info in data['Valute'].items():
            try:
                currency, exist = Currency.objects.get_or_create(
                    charcode=charcode,
                    date=data['Date'],
                    defaults={
                        'charcode': charcode,
                        'date': data['Date'],
                        'rate': info['Value']
                    })
                currency.save()
            except Exception as e:
                logger.error(f'Error occurred while processing currency {charcode}: {e}')
