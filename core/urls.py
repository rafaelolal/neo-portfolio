from django.urls import path

from .views import (
    AwardListView,
    CertificateListView,
    ImageListView,
    ProjectListView,
    SkillListView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path(
        "certificates/", CertificateListView.as_view(), name="certificate_list"
    ),
    path("awards/", AwardListView.as_view(), name="award_list"),
    path("images/", ImageListView.as_view(), name="image_list"),
    path("skills/", SkillListView.as_view(), name="skill_list"),
]
