import os

DJANGO_SETTINGS_MODULE = "portfolio.settings"
APP_NAME = "core"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

import django
django.setup()

from importlib import import_module
models = import_module(f"{APP_NAME}.models")
Project = models.Project

for project in Project.objects.all():
    if (project.start_month == project.end_month and
            project.start_year == project.end_year):
        project.end_month = None
        project.end_year = None
        project.save()
        print(f"[cleaned] {project.name}")
    else:
        print(f"[skipped] {project.name}")

print("\nDone.")
