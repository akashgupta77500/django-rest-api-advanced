from django.db import models


# Create your models here.
class StudentUser(models.Model):
    user = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=10, null=True)
    image = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=10, null=True)
    resume = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user
