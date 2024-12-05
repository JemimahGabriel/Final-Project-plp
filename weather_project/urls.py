from django.contrib import admin
from django.urls import path, include  # 'include' allows including other URL configs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin dashboard
    path('', include('weather_app.urls')),  # Include the weather app's URLs
]
