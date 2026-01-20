from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name="class_name")
def class_name(object):
    return object.__class__.__name__


@register.filter(name="get_project_count")
def get_project_count(skill):
    counts = {"Total": 0,"Small": 0, "Medium": 0, "Large": 0}
    for project in skill.projects.all():
        for size in counts.keys():
            # Always fails on "Total", but that's okay
            if project.tags.filter(name__iexact=size).exists():
                counts[size] += 1
                counts["Total"] += 1

    return counts

@register.filter(name="get_other_count")
def get_other_count(skill):
    other_count = {
        "Certificate": 0,
        "Award": 0,
    }

    found_any = False
    for section in other_count.keys():
        other_count[section] = getattr(skill, f"{section.lower()}s").count()
        if other_count[section] != 0:
            found_any = True

    return other_count if found_any else None

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
