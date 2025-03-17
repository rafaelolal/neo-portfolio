import json
import os

import django
from django.db import transaction

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

# Assuming your Django project is set up and these models are in an app named 'projects'
if True:
    from core.models import (
        Award,
        Certificate,
        Course,
        Image,
        Page,
        Profile,
        Project,
        Skill,
        Tag,
    )  # Replace 'projects' with your app name

# Now you can import Django models after django.setup()


# Now you can import Django models
# For example:
# from your_app.models import YourModel


# Assuming you have the models defined as in your provided code
# and you have a Django environment set up.  This code *must* be run
# within a Django context (e.g., using `manage.py shell` or within a
# Django view/management command).  It will *not* work as a standalone
# Python script without the Django ORM.

month_to_int = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def create_projects_from_json(file_path):
    """
    Creates Django objects (Project, Skill, Image, Tag) from a JSON file.

    Args:
        file_path: The path to the JSON file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    with transaction.atomic():  # Use a transaction for atomicity
        for project_data in data:
            # 1. Create/Get the Project
            project, created = Project.objects.get_or_create(
                name=project_data["title"],
                defaults={
                    "start_month": month_to_int[project_data["start_month"]],
                    "start_year": project_data["start_year"],
                    "description": project_data["description"],
                    "link": project_data.get(
                        "links"
                    ),  # Use get() to handle missing links
                },
            )

            # 2. Create/Get and Associate Skills
            for skill_name in project_data.get(
                "skills", []
            ):  # Handle missing skills
                skill, _ = Skill.objects.get_or_create(name=skill_name)
                project.skills.add(skill)  # ManyToManyField add

            # 3. Create/Get and Associate Images
            for image_path in project_data.get("images", []):
                image, _ = Image.objects.get_or_create(image=image_path)
                project.images.add(image)

            # 4.  Create/Get and Associate Tags
            for tag_name in project_data.get("tags", []):
                if tag_name not in ["featured", "small", "medium", "large"]:
                    print(
                        f"Warning: Invalid tag '{tag_name}' for project '{project.title}'. Skipping."
                    )
                    continue  # Skip invalid tags
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                project.tags.add(tag)

            project.save()  # save the project after adding all related objects.


def create_pages():
    p1 = Page.objects.create(
        name="Projects",
        description="A collection of projects I have worked on.",
        keywords="projects, portfolio, work",
    )

    p2 = Page.objects.create(
        name="About",
        description="A brief description of who I am.",
        keywords="about, me, bio",
    )

    p3 = Page.objects.create(
        name="Contact",
        description="A way to get in touch with me.",
        keywords="contact, email, phone",
    )

    p4 = Page.objects.create(
        name="Courses",
        description="A collection of courses I have taken.",
        keywords="courses, education, classes",
    )

    p5 = Page.objects.create(
        name="Certificates",
        description="A collection of certificates I have earned.",
        keywords="certificates, awards, recognition",
    )

    p6 = Page.objects.create(
        name="Awards",
        description="A collection of awards I have received.",
        keywords="awards, recognition, achievements",
    )

    p7 = Page.objects.create(
        name="Skills",
        description="A collection of skills I have.",
        keywords="skills, abilities, proficiencies",
    )

    p8 = Page.objects.create(
        name="Experience",
        description="A collection of experiences I have had.",
        keywords="experience, work, roles",
    )

    p9 = Page.objects.create(
        name="Education",
        description="A collection of educational experiences I have had.",
        keywords="education, school, university",
    )

    p1.save()
    p2.save()
    p3.save()
    p4.save()
    p5.save()
    p6.save()
    p7.save()
    p8.save()
    p9.save()


def create_achievements_from_json(file_path):
    """
    Creates Django objects (Course, Certificate, Award) from a JSON file.

    Args:
        file_path: The path to the JSON file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    with transaction.atomic():  # Use a transaction for atomicity
        for item_data in data:
            item_type = item_data["type"]

            if item_type == "course":
                Course.objects.get_or_create(
                    name=item_data["name"],
                    defaults={
                        "link": item_data["link"],
                        "description": item_data["description"],
                        "association": item_data["association"],
                        "start_month": item_data["start_month"],
                        "start_year": item_data["start_year"],
                    },
                )
            elif item_type == "certificate":
                Certificate.objects.get_or_create(
                    name=item_data["name"],
                    defaults={
                        "link": item_data["link"],
                        "description": item_data.get("description"),
                        "association": item_data["association"],
                        "start_month": item_data["start_month"],
                        "start_year": item_data["start_year"],
                    },
                )
            elif item_type == "award":
                Award.objects.get_or_create(
                    name=item_data["name"],
                    defaults={
                        "link": item_data.get(
                            "link"
                        ),  # Link is optional for awards
                        "description": item_data.get("description"),
                        "issuer": item_data["issuer"],
                        "start_month": item_data["start_month"],
                        "start_year": item_data["start_year"],
                    },
                )
            else:
                print(f"Warning: Unknown item type '{item_type}'. Skipping.")


def main():
    # Read the JSON data from file
    p1 = Profile.objects.create(
        name="Rafael Almeida",
        description="I am great",
        email="portfolio@ralmeida.dev",
        github="https://github.com/rafaelolal",
        linkedin="https://www.linkedin.com/in/rafaelolal/",
        interests="I like coding",
        doing_now="I am coding",
    )
    i1 = Image.objects.create(
        name="Me",
        description="A picture of me",
        image="images/me.jpg",
    )
    p1.images.add(i1)
    p1.save()
    create_pages()
    create_achievements_from_json("portfolio.achievements.json")
    create_projects_from_json("portfolio.posts.json")


if __name__ == "__main__":
    main()
