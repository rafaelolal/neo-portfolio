# TODO: update this to instead just read all of the models in the module dynamically
# probably using dir() and getattr() or something or apps.get_models()

from django.contrib import admin

from .models import (
    Award,
    Certificate,
    Image,
    Page,
    Profile,
    Project,
    Skill,
)

# Register your models here.

models = [
    Project,
    Certificate,
    Award,
    Image,
    Skill,
    Page,
    Profile,
]

for model in models:
    admin.site.register(model)
