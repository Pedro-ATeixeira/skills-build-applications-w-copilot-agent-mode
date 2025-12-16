from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')
    def test_user_create(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Superman')
    def test_activity_create(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-12-16')
        self.assertEqual(str(activity), 'Iron Man - Running on 2025-12-16')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        self.assertEqual(str(workout), 'Pushups')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Marvel - 100 points')
