from django.urls import path
from . import views
urlpatterns=[
    path("/home",views.home,name="home"),
    path("",views.index,name="index"),
    path("post/<str:post_id>", views.detail,name="detail"),
]