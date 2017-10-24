from django.db import models


class File(models.Model):
    file_content = models.FileField('file_content')
    file_name = models.TextField('file_name', max_length=100, default='untitled')