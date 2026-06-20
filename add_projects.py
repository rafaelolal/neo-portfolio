"""
Standalone import script — run from the Django project root:

    DJANGO_SETTINGS_MODULE=mysite.settings python import_projects.py

Update the two constants below before running:
  - DJANGO_SETTINGS_MODULE: your project's settings module
  - APP_NAME: the Django app that contains the models
  - JSON_PATH: path to all_projects.json (absolute or relative to cwd)
"""

import json
import os
import sys

DJANGO_SETTINGS_MODULE = "portfolio.settings"
APP_NAME = "core"
JSON_PATH = os.path.join(os.path.dirname(__file__), "new_projects.json")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

import django
django.setup()

from importlib import import_module
models = import_module(f"{APP_NAME}.models")
Project = models.Project
Skill = models.Skill
Tag = models.Tag


def main():
    with open(JSON_PATH) as f:
        entries = json.load(f)

    for data in entries:
        fields = {
            "description": data.get("description"),
            "links": data.get("links") or [],
            "association": data.get("association"),
            "start_month": data.get("start_month"),
            "start_year": data.get("start_year"),
            "end_month": data.get("end_month"),
            "end_year": data.get("end_year"),
        }

        project, created = Project.objects.get_or_create(
            name=data["name"],
            defaults=fields,
        )

        if not created:
            for attr, value in fields.items():
                setattr(project, attr, value)
            project.save()

        for skill_name in data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            project.skills.add(skill)

        for tag_name in data.get("tags", []):
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            project.tags.add(tag)

        status = "created" if created else "updated"
        print(f"[{status}] {project.name}")

    print("\nDone.")


if __name__ == "__main__":
    main()
