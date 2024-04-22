from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        help_text=_("Required. email must be unique."),
        error_messages={"unique": _("A user with that email already exists.")},
    )
    profile_image = models.ImageField(default="default.png")
    BVN = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    wallet = models.FloatField(default=0)
    task_earning = models.FloatField(default=0)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
