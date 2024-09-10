from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # 为了让用户能够访问到详情页我们需要在poems/urls.py中添加一个新的路径
    path("details/<int:poem_id>/", views.details, name="details"),
    path("delete/<int:poem_id>/", views.delete, name="delete"),
    path("add/", views.add, name="add"),
    path("edit/<int:poem_id>/", views.edit, name="edit"),
]