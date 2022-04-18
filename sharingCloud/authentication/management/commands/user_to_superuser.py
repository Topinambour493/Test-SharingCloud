from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.contrib.auth.models import User

class Command(BaseCommand):
    help="Add the administrator right to the user to which corresponds the username given in argument."
    def add_arguments(self, parser):
        parser.add_argument('username',type=str)

    def handle(self, *args, **options):
        username = options.get('username')
        try :
            user = User.objects.get(username=username)
            if user.is_superuser == True:
                print(username,"is already superuser")
            else :
                user.is_superuser = True
                user.save()
                print(username,"is now superuser")
        except :
            print(username,"not exist")