from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('api/v1/', include('api.v1.urls')),
]
