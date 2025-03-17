from django.db.models import Count
from django.views.generic import ListView

from .models import (
    Award,
    Certificate,
    Course,
    Education,
    Experience,
    Image,
    Page,
    Project,
    Skill,
)


class BaseListView(ListView):
    template_name = "list.html"
    context_object_name = "objects"
    paginate_by = 12

    def get_queryset(self):
        objects = (
            super()
            .get_queryset()
            .order_by("-start_month")
            .order_by("-start_year")
        )
        tag = self.request.GET.get("tag")
        if tag:
            return objects.filter(tags__name__iexact=tag)

        return objects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model.__name__

        page_obj = context.get("page_obj")
        if page_obj:
            paginator = context.get("paginator")
            current_page = page_obj.number

            start_page = max(current_page - 2, 1)
            end_page = min(current_page + 2, paginator.num_pages)

            context["page_range"] = range(start_page, end_page + 1)

            query_params = self.request.GET.copy()
            if "page" in query_params:
                del query_params["page"]
            context["query_string"] = query_params.urlencode()

        context |= self.get_page_data()
        return context

    def get_page_data(self):
        wanted_page_name = self.model.__name__
        page = Page.objects.filter(name__contains=wanted_page_name).first()
        if not page:
            return {}

        return {
            "page": page,
        }


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

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                total_count=(
                    Count("projects")
                    + Count("awards")
                    + Count("certificates")
                    + Count("courses")
                    + Count("educations")
                    + Count("experiences")
                )
            )
            .order_by("-total_count")
        )
