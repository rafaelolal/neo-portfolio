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

    s = f"Projects: {counts[0][1]} small, {counts[1][1]} medium, {counts[2][1]} large"

    return s


@register.filter(name="get_section_count")
def get_section_count(skill) -> list[tuple[str, int]]:
    sections = [
        ["Certificate", 0],
        ["Award", 0],
    ]

    found_any = False
    for section in sections:
        section[1] = getattr(skill, f"{section[0].lower()}s").count()
        if section[1] != 0:
            found_any = True

    s = f"Other: {sections[0][1]} certificates, {sections[1][1]} awards"
    return s if found_any else []


@register.simple_tag(name="get_navbar_urls")
def get_navbar_urls():
    urls = (
        ("Projects", reverse("project_list")),
        ("Skills", reverse("skill_list")),
        ("Awards", reverse("award_list")),
        ("Certificates", reverse("certificate_list")),
    )

    # return "hello"
    return urls


@register.filter(name="month_name")
def month_name(month_number: int) -> str:
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    if 1 <= month_number <= 12:
        return months[month_number - 1]

    return ""
