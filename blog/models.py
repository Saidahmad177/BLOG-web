from django.db import models


# Create your models here.
class Yangilik(models.Model):

    class Status(models.TextChoices):
        draft = 'DF', 'Draft'
        published = 'PB', 'Published'

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    publish_date = models.DateTimeField()
    create_time = models.DateTimeField()
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.draft
                              )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']
