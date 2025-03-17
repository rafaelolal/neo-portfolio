from django.views.generic import TemplateView

from .models import Image, Page, Profile


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = Profile.objects.first()
        context["image"] = Image.objects.filter(name__iexact="Me").first()
        context["page"] = Page.objects.filter(name__iexact="About").first()
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = Profile.objects.first()
        context["page"] = Page.objects.filter(name__iexact="Contact").first()

        return context
