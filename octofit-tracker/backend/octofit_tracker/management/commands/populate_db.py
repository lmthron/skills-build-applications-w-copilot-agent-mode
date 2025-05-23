import sys
import os
import django
from django.conf import settings

if not settings.configured:
    django.setup()


from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        print('populate_db command loaded')
        print('Python path:', sys.path)
        # Adding test data for users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=30)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=25)

        # Adding test data for teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Adding test data for activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-22')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-22')

        # Adding test data for leaderboard
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=150)

        # Adding test data for workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60)
        Workout.objects.create(name='HIIT Training', description='High-intensity interval training', duration=30)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
