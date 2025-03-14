from django.db import models

# Create your models here.


class Me(models.Model):
    email = models.EmailField(unique=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
