from django.urls import path
from stkpush import views

app_name = "stkpush"

urlpatterns = [
    path('pay/', views.pay, name="pay"),
    path('stk/', views.stk)
]