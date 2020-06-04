from django.db import models


# Create your models here.

class ReviewCustomer(models.Model):
    comment = models.TextField(blank=True)
    customer_name = models.CharField(max_length=50)
    customer_job = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)
    customer_image = models.ImageField(upload_to='customer_image')

    def __str__(self):
        return self.customer_name
