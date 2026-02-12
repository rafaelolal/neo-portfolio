import json
import os

import django
from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

# Putting an if-statement to avoid auto import organization
if True:
    from core.models import (
        Award,
        Certificate,
        Image,
        Page,
        Profile,
        Project,
        Skill,
        Tag,
    )

models = [Award, Certificate, Image, Page, Profile, Project, Skill, Tag]

for model in models:
    with transaction.atomic():
        for obj in model.objects.all():
            link = getattr(obj, "link", None)
            github_repo = getattr(obj, "github_repo", None)
            links = []
            if link:
                links.append(link)
            if github_repo:
                links.append(github_repo)

            if links:
                obj.links = links
                obj.save()
            
            print(f"Updated {model.__name__} id={obj.id} with links: {links}")

