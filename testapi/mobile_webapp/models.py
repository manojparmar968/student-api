from django.db import models

# Create your models here.

# Students Detail
class Students(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    DOB = models.DateField(max_length=8)
    mobile_number = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Students'
