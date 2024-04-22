from rest_framework.views import APIView
from .serializer import UserRegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "error":False, "message":"registration successful", "data":serializer.data}, status.HTTP_201_CREATED)
        return Response({"success":False, "error":True, "message":"registration unsuccessful", "data":serializer.errors}, status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    serialize_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"success": False}, status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response({"success": True, "data": serializer.data})

    def patch(self, request, id,):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"success": False}, status.HTTP_406_NOT_ACCEPTABLE)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message":"Profile updated successfully", "data": serializer.data})
        return Response({"success": False}, status.HTTP_406_NOT_ACCEPTABLE)


class VerificationView(APIView):
    pass
