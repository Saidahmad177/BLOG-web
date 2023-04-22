from django.db import models
from django.utils import timezone

from users.models import CustomUser


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=New.Status.published)


class New(models.Model):

    class Status(models.TextChoices):
        draft = 'DF', 'Draft'
        published = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.draft
                              )

    published = PublishManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']

class Comments(models.Model):
    blog = models.ForeignKey(New, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.username
