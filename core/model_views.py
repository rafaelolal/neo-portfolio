from django.views.generic import ListView

from .models import (
    Award,
    Certificate,
    Course,
    Education,
    Experience,
    Image,
    Project,
    Skill,
)


class BaseListView(ListView):
    template_name = "list.html"
    context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model.__name__
        return context


class ProjectListView(BaseListView):
    model = Project


class ExperienceListView(BaseListView):
    model = Experience


class CertificateListView(BaseListView):
    model = Certificate


class EducationListView(BaseListView):
    model = Education


class CourseListView(BaseListView):
    model = Course


class AwardListView(BaseListView):
    model = Award


class ImageListView(BaseListView):
    model = Image


class SkillListView(BaseListView):
    model = Skill
