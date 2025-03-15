from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    MONTHS = (
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    association = models.CharField(max_length=255, blank=True, null=True)
    start_month = models.IntegerField(choices=MONTHS)
    start_year = models.IntegerField()
    end_month = models.IntegerField(choices=MONTHS, blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    images = models.ManyToManyField(
        "Image", related_name="projects", blank=True
    )
    skills = models.ManyToManyField(
        "Skill", related_name="projects", blank=True
    )

    def __str__(self):
        return self.name


class Experience(BaseModel):
    EMPLYMENT_TYPES = (
        ("full_time", "Full-time"),
        ("part_time", "Part-time"),
        ("self_employed", "Self-employed"),
        ("freelance", "Freelance"),
        ("contract", "Contract"),
        ("internship", "Internship"),
        ("apprenticeship", "Apprenticeship"),
        ("volunteer", "Volunteer"),
    )
    LOCATION_TYPES = (
        ("remote", "Remote"),
        ("onsite", "On-site"),
        ("hybrid", "Hybrid"),
    )

    title = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255, choices=EMPLYMENT_TYPES)
    company = models.CharField(max_length=255)
    start_month = models.IntegerField(choices=Project.MONTHS)
    start_year = models.IntegerField()
    end_month = models.IntegerField(
        choices=Project.MONTHS, blank=True, null=True
    )
    end_year = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255)
    location_type = models.CharField(max_length=255, choices=LOCATION_TYPES)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    images = models.ManyToManyField(
        "Image", related_name="experiences", blank=True
    )
    skills = models.ManyToManyField(
        "Skill", related_name="experiences", blank=True
    )


class Education(BaseModel):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_month = models.IntegerField(choices=Project.MONTHS)
    start_year = models.IntegerField()
    end_month = models.IntegerField(
        choices=Project.MONTHS, blank=True, null=True
    )
    end_year = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    activities = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(
        "Skill", related_name="educations", blank=True
    )
    images = models.ManyToManyField(
        "Image", related_name="educations", blank=True
    )


class Certificate(BaseModel):
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    issue_month = models.IntegerField(choices=Project.MONTHS)
    issue_year = models.IntegerField()
    expiration_month = models.IntegerField(
        choices=Project.MONTHS, blank=True, null=True
    )
    expiration_year = models.IntegerField(blank=True, null=True)
    credential_id = models.CharField(max_length=255, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(
        "Skill", related_name="certificates", blank=True
    )
    images = models.ManyToManyField(
        "Image", related_name="certificates", blank=True
    )

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    association = models.CharField(max_length=255, blank=True, null=True)


class Award(BaseModel):
    name = models.CharField(max_length=255)
    association = models.CharField(max_length=255, blank=True, null=True)
    issuer = models.CharField(max_length=255, blank=True, null=True)
    issue_month = models.IntegerField(choices=Project.MONTHS)
    issue_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    images = models.ManyToManyField("Image", related_name="awards", blank=True)

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(upload_to="images/")
    alt = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.alt


class Skill(BaseModel):
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
