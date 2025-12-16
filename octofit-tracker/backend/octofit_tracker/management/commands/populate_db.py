from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in safe order
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
        ]

        # Create activities
        for user in users:
            Activity.objects.create(user=user, type='Running', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, type='Cycling', duration=45, date=timezone.now().date())

        # Create workouts
        workout1 = Workout.objects.create(name='Hero Strength', description='Strength workout for heroes')
        workout2 = Workout.objects.create(name='Speed Training', description='Speed workout for heroes')
        workout1.suggested_for.set(users)
        workout2.suggested_for.set(users)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=100, week='2025-W50')
        Leaderboard.objects.create(team=dc, total_points=120, week='2025-W50')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
