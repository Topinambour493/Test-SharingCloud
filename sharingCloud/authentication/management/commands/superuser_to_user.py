from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.contrib.auth.models import User

class Command(BaseCommand):
    help="remove the administrator right to the user to which corresponds the username given in argument."
    def add_arguments(self, parser):
        parser.add_argument('username',type=str)

    def handle(self, *args, **options):
        username = options.get('username')
        try :
            user = User.objects.get(username=username)
            if user.is_superuser == False:
                print(username,"is already user")
            else :
                user.is_superuser = False
                user.save()
                print(username,"is now user")
        except :
            print(username,"not exist")