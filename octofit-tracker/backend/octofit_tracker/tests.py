from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, activity='Run', duration=10)
        self.assertEqual(str(activity), 'Test User - Run')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=42)
        self.assertEqual(str(leaderboard), 'Test User - 42')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        workout = Workout.objects.create(user=user, workout='Pushups', reps=20)
        self.assertEqual(str(workout), 'Test User - Pushups')
