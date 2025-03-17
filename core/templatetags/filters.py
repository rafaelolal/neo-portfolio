from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name="class_name")
def class_name(object):
    return object.__class__.__name__


@register.filter(name="get_project_count")
def get_project_count(skill):
    counts = [["Small", 0], ["Medium", 0], ["Large", 0]]
    for project in skill.projects.all():
        for count in counts:
            if project.tags.filter(name__iexact=count[0]).exists():
                count[1] += 1

    return counts


@register.filter(name="get_section_count")
def get_section_count(skill):
    sections = [
        ["Award", 0],
        ["Certificate", 0],
        ["Course", 0],
        ["Education", 0],
        ["Experience", 0],
    ]
    for section in sections:
        section[1] = getattr(skill, f"{section[0].lower()}s").count()

    return sections


@register.simple_tag(name="get_navbar_urls")
def get_navbar_urls(_=""):
    urls = (
        ("Projects", reverse("project_list")),
        ("Experiences", reverse("experience_list")),
        ("Education", reverse("education_list")),
        ("Skills", reverse("skill_list")),
        ("Awards", reverse("award_list")),
        ("Courses", reverse("course_list")),
        ("Certificates", reverse("certificate_list")),
        ("About", reverse("about")),
        ("Contact", reverse("contact")),
    )

    return urls
