from django.urls import path
from stkpush import views

app_name = "stkpush"

urlpatterns = [
    path('', views.home, name="home"),
    path('pay/', views.pay, name="pay"),
    path('stk/', views.stk, name="stk")
]