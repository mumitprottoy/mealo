from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Families'




class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    # privileges
    admin = models.BooleanField(default=False)

    