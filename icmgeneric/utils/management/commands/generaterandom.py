from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generates random secret key for django'

    def handle(self, *args, **options):
        import random
        SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
        print SECRET_KEY
