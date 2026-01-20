from django.db.models import Count
from django.views.generic import ListView

from .models import (
    Award,
    Certificate,
    Image,
    Profile,
    Project,
    Skill,
    Page,
)


class BaseListView(ListView):
    template_name = "list.html"
    context_object_name = "objects"

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
        context["about"] = Profile.objects.first()
        context["model_name"] = self.model.__name__
        context["page"] = Page.objects.filter(name__iexact=self.model.__name__ + "s").first()

        return context


class ProjectListView(BaseListView):
    model = Project


class CertificateListView(BaseListView):
    model = Certificate


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
                    Count("projects") + Count("awards") + Count("certificates")
                )
            )
            .order_by("-total_count")
        )