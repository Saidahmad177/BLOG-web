from django.db import models
from django.utils import timezone


class New(models.Model):

    class Status(models.TextChoices):
        draft = 'DF', 'Draft'
        published = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.draft
                              )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']
