from rest_framework.views import APIView
from .serializer import TaskSerializer, P2PSerilizer
from .models import Task, P2P_transactions
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User


class AllTaskView(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs) -> Response:
        self.option = self.kwargs["option"]

        if str(self.option) == "both":
            task = Task.objects.all()
        elif str(self.option) == "verified":
            task = Task.objects.filter(verified_or_unverified="verified")
        elif str(self.option) == "create":
            return Response({"success": True, "message": "Create post"})
        else:
            try:
                user = User.objects.get(username=str(self.option))
                task = Task.objects.filter(username=user.username)
            except:
                return Response({"success": False, "message": "not a valied route"})

        serializer = TaskSerializer(task, many=True)
        return Response({"success": True, "data": serializer.data})

    def post(self, request, *args, **kwargs) -> Response:
        self.option = self.kwargs["option"]

        if str(self.option) == "create":
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                user = User.objects.get(username=serializer.validated_data["username"])
                if user.wallet >= float(serializer.validated_data["amount"]):
                    return Response(
                        {
                            "success": False,
                            "message": "you do not have sufficent balance for this task",
                            "errors": serializer.errors,
                        }
                    )
                else:
                    serializer.save(user_images=user.profile_image)
                    return Response(
                        {
                            "success": True,
                            "message": "Task created successfully",
                            "data": serializer.data,
                        }
                    )
            else:
                return Response(
                    {
                        "success": False,
                        "message": "Invalid data provided",
                        "errors": serializer.errors,
                    }
                )
        else:
            return Response(
                {"success": False, "message": "Task creation was not succesfull"}
            )


class TaskView(APIView):
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs) -> Response:
        self.id = self.kwargs["id"]

        try:
            task = Task.objects.get(id=self.id)
        except:
            return Response(
                {"success": False, "message": "Task with that id does not exist"}
            )

        serializer = TaskSerializer(task)
        return Response({"success": True, "data": serializer.data})

    def patch(self, request, *args, **kwargs) -> Response:
        self.id = self.kwargs["id"]

        try:
            task = Task.objects.get(id=self.id)
        except:
            return Response(
                {"success": False, "message": "Task with that id does not exist"}
            )

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "message": "Task update successfullyt",
                }
            )
        else:
            return Response(
                {
                    "success": False,
                    "data": serializer.errors,
                    "message": "Task update unsuccessfully",
                }
            )

        return Response({"success": False}, status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, *args, **kwargs) -> Response:
        self.id = self.kwargs["id"]

        try:
            task = Task.objects.get(id=self.id)
        except:
            return Response(
                {"success": False, "message": "Task with that id does not exist"}
            )
        task.delete()
        return Response({"success": True, "message": "Task delete successfully"})


class P2p_view(APIView):
    serializer_class = P2PSerilizer

   
    def post(self, request, *args, **kwargs) -> Response:
        serializer = P2PSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {{"success":True, "message":"Task accepted", "data":serializer.data}})
        else:
            return Response(
                {"success":False, "message":"unable to accept task", "data":serializer.errors}
            )





class P2p_userView(APIView):
    serializer_class = P2PSerilizer

    def get(self, request, *args,**kwargs) -> Response:
        self.task_username = self.kwargs["username"]
        self.task_option = self.kwargs["option"]
        # self.task_all = self.kwargs["all"]

        if self.task_option == "owner":
            try:
                self.username = User.objects.get(username=self.task_username)
                print(self.username.id)
            except :
                return Response(
                     {"success":False, "message":"User does not exist"}
                )
            try:
                owner = P2P_transactions.objects.filter(task_owner=self.username.id)
            except :
                return Response(
                    {"success":False, "message":"you do not have access to this transaction"}
                )
            serializer = P2PSerilizer(owner, many=True)
            return Response(
                {"success":True, "data":serializer.data}
            )
        elif self.task_option == "handler":
            try:
                handler = P2P_transactions.objects.filter(task_handler="admin")
            except :
                return Response(
                    {"success":False, "message":"you do not have access to this transaction"}
                )
            print(handler)
            serializer = P2PSerilizer(handler, many=True)
            return Response(
                {"success":True, "data":serializer.data}
            )
        else:
            return Response(
                    {"success":False, "message":"you do not have access to this transaction"}
                )



    

    def patch(self, request,args, **kwargs) -> Response:
        pass





class P2p_transactionView(APIView):
    serializer_class = P2PSerilizer

    def get(self, request, *args, **kwargs) -> Response:
        self.id = self.kwargs["id"]

        try:
            transaction = P2P_transactions.objects.get(id=self.id)
        except:
            return Response(
                {"success": False, "message": "Transaction with this id does not exist"}
            )
        serializer = P2PSerilizer(transaction)
        return Response({"success": True, "data": serializer.data})

    def patch(self, request, *args, **kwargs) -> Response:
        self.id = self.kwargs["id"]

        try:
            transaction = P2P_transactions.objects.get(id=self.id)
        except:
            return Response(
                {"success": False, "message": "Transaction with this id does not exist"}
            )
        serializer = P2PSerilizer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "transaction update successfully",
                    "data": serializer.data,
                }
            )
        else:
            return Response(
                {"success":False, "message":"transaction update not successfull", "data":serializer.errors}
            )
        return Response(
            {"success":False,}
        )
