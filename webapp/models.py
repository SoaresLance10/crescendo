from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Intra_participant(models.Model):
    paticipants_id = models.AutoField(primary_key=True, unique=True)
    name = models.TextField(max_length=100)
    roll_no = models.IntegerField()
    class_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    groups = models.CharField(default='participant', max_length=100)

    def __str__(self):
        return f"Roll No:{self.roll_no} Name:{self.name}"

class Inter_participant(models.Model):
    paticipants_id = models.AutoField(primary_key=True, unique=True)
    name = models.TextField(max_length=100)
    college_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    groups = models.CharField(default='participant', max_length=100)

    def __str__(self):
        return f"ID:{self.paticipants_id} Name:{self.name}"

class Council(models.Model):
    council_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 100)
    name = models.CharField(max_length=100)
    groups = models.CharField(default='council', max_length=100)

    def __str__(self):
        return f"Username:{self.username} Council ID:{self.council_id} Name:{self.name}"

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    council_id = models.IntegerField()
    img = models.CharField(max_length = 100, default = "static/webapp/assets/images/profile.svg")
    total_reg = models.IntegerField()
    team = models.IntegerField(default=0)
    class_cap = models.IntegerField(default=100)

    def __str__(self):
        return f"Council ID:{self.council_id} Event ID:{self.event_id} Name:{self.name}"

class Registration(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=100)
    event_id = models.IntegerField()
    council_id = models.IntegerField()
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"Participant ID:{self.p_id} Name:{self.p_name} Event ID:{self.event_id} Council ID: {self.council_id}"

class TeamRegistration(models.Model):
    team_id = models.AutoField(primary_key=True)
    p1_id = models.IntegerField()
    p2_id = models.IntegerField(blank=True, null=True)
    p3_id = models.IntegerField(blank=True, null=True)
    p1_name = models.CharField(max_length=100)
    p2_name = models.CharField(max_length=100, blank=True, null=True)
    p3_name = models.CharField(max_length=100, blank=True, null=True)
    class_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.class_name}: {self.p1_name} {self.p2_name} {self.p3_name}"

class Score(models.Model):
    class_name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"Class: {self.class_name} Score: {self.score}"