"""math_battle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from api import views

from upload.views import image_upload

urlpatterns = [
    path("api/status", views.api_status, name="status"),  # GET
    path("api/create_session", views.create_session, name="create_session"),  # POST
    path("api/sessions/", views.get_sessions, name="get_sessions"),  # GET
    path("api/session/<str:session_id>/user", views.add_user_to_session, name="add_user_to_session"),  # PUT
    path("api/session/<str:session_id>/user/<int:user_id>/problem", views.get_new_problem, name="get_new_problem"),  # GET
    path("api/session/<str:session_id>/user/<int:user_id>/solution", views.submit_problem_solution, name="submit_problem_solution"),  # POST
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path("upload", image_upload, name="upload"))
    urlpatterns.append(path('admin', admin.site.urls))
