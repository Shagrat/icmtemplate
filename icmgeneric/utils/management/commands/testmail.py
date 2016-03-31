from django.core.management.base import BaseCommand
from django.core.mail import send_mail


class Command(BaseCommand):
    args = '<email email ...>'
    help = 'Sends test mail from this site'

    def handle(self, *args, **options):
        try:
            from settings import DEFAULT_FROM_EMAIL
            for email in args:
                send_mail('Test mail', 'Please respond to sfunin@gmail.com if you got this email', DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        except:
            print "Somthing gone wrong:("
