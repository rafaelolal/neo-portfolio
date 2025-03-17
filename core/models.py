from django.db import models


class BaseModel(models.Model):
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    association = models.CharField(max_length=255, blank=True, null=True)

    start_month = models.IntegerField(choices=MONTHS, blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(choices=MONTHS, blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class Image(BaseModel):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.name} - {self.description}"


class Skill(BaseModel):
    proficiency = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    def __str__(self):
        return self.name


class WithImageSkillTag(models.Model):
    images = models.ManyToManyField(
        Image,
        blank=True,
        related_name="%(class)ss",
    )
    skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="%(class)ss",
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="%(class)ss",
    )

    class Meta:
        abstract = True


class Profile(BaseModel, WithImageSkillTag):
    interests = models.TextField(blank=True, null=True)
    doing_now = models.TextField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Page(BaseModel):
    keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(BaseModel, WithImageSkillTag):
    def __str__(self):
        return self.name


class Experience(BaseModel, WithImageSkillTag):
    EMPLOYMENT_TYPES = (
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

    employment_type = models.CharField(
        max_length=255, choices=EMPLOYMENT_TYPES
    )
    location = models.CharField(max_length=255)
    location_type = models.CharField(max_length=255, choices=LOCATION_TYPES)

    def __str__(self):
        return f"{self.name} - {self.association} - {self.start_year}/{self.start_month} - {self.end_year}/{self.end_month}"


class Education(BaseModel, WithImageSkillTag):
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    grade = models.CharField(max_length=255, blank=True, null=True)
    activities = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Certificate(BaseModel, WithImageSkillTag):
    credential_id = models.CharField(max_length=255, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Course(BaseModel, WithImageSkillTag):
    number = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.number}"


class Award(BaseModel, WithImageSkillTag):
    issuer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
