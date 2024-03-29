import logging

from django.core.management.base import BaseCommand

from app.catalogs.tasks import load_currencies

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Loads currency data from external source'

    def handle(self, *args, **kwargs):
        try:
            load_currencies()
        except Exception as e:
            logger.exception(e)
            self.stdout.write(self.style.ERROR('Error loading currencies'))
        else:
            self.stdout.write(self.style.SUCCESS('Successfully initiated currency data loading'))
