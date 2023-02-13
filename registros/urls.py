from django.urls import path

from . import views

app_name = "registros"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cadastro-abate/", views.TestFormView.as_view(), name="cadastro_abate"),
]
