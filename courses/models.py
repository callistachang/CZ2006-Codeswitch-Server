from django.db import models
from skills.models import Skill

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    organizer = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    course_src = models.URLField(max_length=200)
    picture_src = models.URLField(blank=True, null=True, max_length=200)
    date_posted = models.DateField()
    skills_taught = models.ManyToManyField(Skill)