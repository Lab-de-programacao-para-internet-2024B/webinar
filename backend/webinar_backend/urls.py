from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("api/auth/", include('user.urls')),
    path("api/courses/", include('courses.urls')),
    path("api/perms/", include('permissions.urls'))
]
