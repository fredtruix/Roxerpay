from django.urls import path
from .apis import AllTaskView, TaskView, P2p_transactionView, P2p_view, P2p_userView

urlpatterns = [
    path('accept/', P2p_view.as_view(), name="accept"),
    path('<str:option>/', AllTaskView.as_view(), name="task"),
    path('detail/<str:id>/', TaskView.as_view(), name="task_id"),
    path('transaction/<str:id>/', P2p_transactionView.as_view(), name="transaction"),
    path('transaction/<str:username>/<str:option>/', P2p_userView.as_view(), name="p2p_user"),
    path('transaction/<str:username>/str:option>/<str:type>/',  P2p_userView.as_view(), name="p2p_users")

]