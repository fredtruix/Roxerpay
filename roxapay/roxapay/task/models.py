from django.db import models
from users.models import User

# Create your models here.

verify = (
    ("both","both"),
    ("verified","verified"),
    ("not verified","not verified")
)


class Task(models.Model):
    username_id = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=300, blank=True, null=True)
    user_images = models.ImageField(default="default.png")
    title = models.CharField(max_length=200)
    description = models.TextField()
    verified_or_unverified = models.CharField(choices = verify , max_length=200, default="both")
    pay = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    task_image = models.ImageField(default="background.jpg")
    task_attendance = models.ManyToManyField(User, related_name='attendance', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    partakers = models.IntegerField(default=0)
    period = models.CharField(max_length=200, blank=True, null=True)
    number = models.IntegerField(default=0)

    class Meta:
        ordering =['-updated', '-created']

    def __str__(self):
        return f'{self.title} created by {self.username}'



class P2P_transactions(models.Model):
    task_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    task_owner_name = models.CharField(max_length=200, blank=True, null=True)
    task_handler = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pay = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    created = models.DateTimeField(auto_now=True)
    owner_accept = models.BooleanField(default=False)
    owner_cancel = models.BooleanField(default=False)
    handler_complete = models.BooleanField(default=False)
    handler_cancel = models.BooleanField(default=False)
    period = models.CharField(max_length=200)
    number = models.IntegerField(default=0)


    def __str__(self):
        ordering = ['-created']

    def __str__(self):
        return f"{self.task_handler} accept {self.title} in {self.number} {self.period}"
