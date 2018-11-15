from django.urls import path

from . import views

urlpatterns = [
    path('grab-favicons', views.GrabiconView.as_view(), name='grab-endpoint'),
    path('grab-favicons/', views.GrabiconView.as_view(), name='grab-endpoint-2'),
]
