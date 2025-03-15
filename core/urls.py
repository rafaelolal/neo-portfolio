from django.urls import path

from .model_views import (
    AwardListView,
    CertificateListView,
    EducationListView,
    ExperienceListView,
    ImageListView,
    ProjectListView,
    SkillListView,
)
from .views import AboutView, ContactView

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("experiences/", ExperienceListView.as_view(), name="experience_list"),
    path(
        "certificates/", CertificateListView.as_view(), name="certificate_list"
    ),
    path("education/", EducationListView.as_view(), name="education_list"),
    path("awards/", AwardListView.as_view(), name="award_list"),
    path("images/", ImageListView.as_view(), name="image_list"),
    path("skills/", SkillListView.as_view(), name="skill_list"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
]
