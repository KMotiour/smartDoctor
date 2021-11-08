
from django.urls import path, include
from .views import ChemberView, ChemberRUDView, ChemberSettingsRUDView, ChemberScheduleRUDView


urlpatterns = [

    path("<str:chember>/", ChemberView.as_view(), name="createChember"),
    path("chemberRUD/<int:pk>", ChemberRUDView.as_view(), name="ChemberRUDView"),
    path("chemberSettingsRUDView/<int:pk>", ChemberSettingsRUDView.as_view(), name="ChemberSettingsRUDView"),
    path("chemberScheduleRUDView/<int:pk>", ChemberScheduleRUDView.as_view(), name="ChemberScheduleRUDView"),

] 
