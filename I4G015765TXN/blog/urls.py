from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="all"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("delete/<slug:slug>", views.PosDeleteView.as_view(), name="post_delete"),
    path("update/<slug:slug>", views.PosUpdateView.as_view(), name="post_update"),
    path("read/<slug:slug>", views.PosDetailView.as_view(), name="post_detail"),

]