from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_customer, name="create_customer"),
    path("interact/<int:id>", views.interact, name="interact"),
    path("summary/", views.summary, name="summary"),
]