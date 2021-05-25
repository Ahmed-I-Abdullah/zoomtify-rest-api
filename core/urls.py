from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meetings.urls', namespace='meetings')),
    path('api', include('api.urls', namespace='api')),
]
