from core.views import JobListCreateAPI, UserTestAPI, home_api
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_api),
    path('api/users/', UserTestAPI.as_view(), name='user-test-api'),
    path('api/jobs/', JobListCreateAPI.as_view(), name='job-list-create-api'),
]