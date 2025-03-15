from django.contrib import admin

from .models import (
    Award,
    Certificate,
    Course,
    Education,
    Experience,
    Image,
    Project,
    Skill,
)

# Register your models here.

models = [
    Project,
    Experience,
    Education,
    Certificate,
    Course,
    Award,
    Image,
    Skill,
]

for model in models:
    admin.site.register(model)
