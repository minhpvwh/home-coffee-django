from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=300)
    description = models.TextField()
    num_lesson = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='course_picture')

    def __str__(self):
        return self.name
