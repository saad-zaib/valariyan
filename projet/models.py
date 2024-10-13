from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    long_description = models.TextField()
    tech = models.ManyToManyField(Technology, related_name='projects', blank=True)
    github = models.URLField(blank=True, null=True)
    live = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='project_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title
