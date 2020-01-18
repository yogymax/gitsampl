
from django.contrib import admin
from django.urls import path

# http://localhost:8000/admin/
urlpatterns = [
    path('admin/', admin.site.urls),
]
