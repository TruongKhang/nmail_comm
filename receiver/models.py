from django.db import models

# Create your models here.


class ModelFile(models.Model):
    file_type = models.CharField(max_length=100)
    # file_path = models.FilePathField(path='./')
    file_field = models.FileField(upload_to='uploads/')