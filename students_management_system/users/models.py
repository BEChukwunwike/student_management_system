from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    def clean(self):
        super().clean()
        if sum([self.is_student, self.is_admin, self.is_lecturer]) > 1:
            raise ValidationError("A user can only be a student, admin, or lecturer, not more than one.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)