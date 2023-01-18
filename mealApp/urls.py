
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('nimda/', admin.site.urls),
    path('', include('entrance.urls')),
]
