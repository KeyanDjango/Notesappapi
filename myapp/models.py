from django.db import models
from django.conf import settings
# Create your models here.


class NoteModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=30)
    content = models.CharField(max_length=600)


    def __str__(self):
        return self.title