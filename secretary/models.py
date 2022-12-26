from django.db import models

# Create your models here.
from django_fsm import FSMField, transition

class BlogPost(models.Model):
    state = FSMField(default='new')

