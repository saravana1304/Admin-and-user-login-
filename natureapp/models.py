from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Natural(models.Model):
    nature_name = models.CharField(max_length=200)
    nature_img = models.ImageField(upload_to='nat')
    nature_country = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nature_name
    





































User = get_user_model()