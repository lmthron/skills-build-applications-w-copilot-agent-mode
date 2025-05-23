from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('User')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.name}"

    class Meta:
        app_label = 'octofit_tracker'


class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

    class Meta:
        app_label = 'octofit_tracker'


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'
