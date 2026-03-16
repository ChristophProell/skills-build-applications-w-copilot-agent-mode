from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Daten löschen
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Tony Stark', team='marvel')
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Peter Parker', team='marvel')
        batman = User.objects.create(email='batman@dc.com', name='Bruce Wayne', team='dc')
        superman = User.objects.create(email='superman@dc.com', name='Clark Kent', team='dc')

        # Activities
        Activity.objects.create(user=ironman.email, activity_type='run', duration=30, date=date(2023, 1, 1))
        Activity.objects.create(user=spiderman.email, activity_type='cycle', duration=45, date=date(2023, 1, 2))
        Activity.objects.create(user=batman.email, activity_type='swim', duration=60, date=date(2023, 1, 3))
        Activity.objects.create(user=superman.email, activity_type='fly', duration=120, date=date(2023, 1, 4))

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Situps', description='Do 30 situps', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='medium')
        Workout.objects.create(name='Burpees', description='Do 15 burpees', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('Testdaten erfolgreich in octofit_db eingefügt.'))
