from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/",views.create,name="create"),
    path("customer/<int:id>",views.products,name="product"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete")
]