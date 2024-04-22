from django.contrib import admin
from .models import Task, P2P_transactions

# Register your models here.
admin.site.register(Task)
admin.site.register(P2P_transactions)
