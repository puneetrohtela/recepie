import time

from django.db import connections
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """waiting for db to connect"""
        self.stdout.write("waiting for db to connect")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write("Database is Unavailable,wating 1 Second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
