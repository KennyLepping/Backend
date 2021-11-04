from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify


class Hero(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Heroes'

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    blurb = models.TextField(blank=True)
    project_url = models.URLField(help_text='The url that links to the actual project\'s website.')
    file = models.FileField(upload_to='project_files/', null=True, blank=True)
    # media/project_images/my_project.png or whatever
    image = models.ImageField(upload_to='project_images/', blank=True)
    secondary_image = models.ImageField(upload_to='project_images/', blank=True)
    is_logo_image = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean(self):
        # Converts name to a slug if not already a valid slug
        self.slug = slugify(self.name) if not self.slug or self.slug != slugify(self.name) else self.slug

    def save(self, *args, **kwargs):
        self.full_clean()  # Calls clean() when saving data in the DB
        super().save(*args, **kwargs)
