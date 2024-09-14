"""
URL configuration for Ems_program project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path ('', home, name='home'),
    # path('', views.view_employees, name='view_employees'),
    # path('add/', views.add_employee, name='add_employee'),
    # path('update/<str:emp_id>/', views.update_employee, name='update_employee'),
    # path('delete/<str:emp_id>/', views.delete_employee, name='delete_employee'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('employees.urls')),
# ]
