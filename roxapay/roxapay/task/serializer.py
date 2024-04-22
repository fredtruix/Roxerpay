from rest_framework import serializers
from .models import Task, P2P_transactions


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "id",
            "username",
            "username_id",
            "user_images",
            "title",
            "description",
            "verified_or_unverified",
            "pay",
            "amount",
            "task_attendance",
            "task_image",
            "created",
            "updated",
            "partakers",
            "period",
            "number"
        ]


class P2PSerilizer(serializers.ModelSerializer):

    class Meta:
        model = P2P_transactions
        fields = [
            "id","task_owner","task_handler","task_owner_name","title","description","pay","amount", "created","owner_accept","owner_cancel","handler_complete","handler_cancel","period","number"
        ]
