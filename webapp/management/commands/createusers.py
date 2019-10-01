from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Home sample refreshcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        for i in range(1,10):
            User.objects.create_superuser(username='testuser'+str(i),password='welcome',email='testuser'+str(i)+'@gmail.com').save()
        return "Successfully create "+str(len(User.objects.all()))+" superusers"