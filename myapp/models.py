from django.db import models

# Create your models here.


class NoteModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=600)


    def __str__(self):
        return self.title