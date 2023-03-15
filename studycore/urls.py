"""studycore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

import user_cust_auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', user_cust_auth.views.StudentModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('studentapi/<int:pk>', user_cust_auth.views.StudentModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                                  'patch': 'partial_update',
                                                                                  'delete': 'destroy'})),
    path('studentsession/', user_cust_auth.views.StudentSession.as_view({'get': 'list', 'post': 'create'})),
    path('studentsession/<int:pk>', user_cust_auth.views.StudentSession.as_view({'get': 'retrieve', 'put': 'update',
                                                                                 'patch': 'partial_update',
                                                                                 'delete': 'destroy'})),
    path('auth/', include('rest_framework.urls')),
    path('auth/setsession/', user_cust_auth.views.CreateSession.as_view()),
    path('SetCSRF', user_cust_auth.views.GetCSRFToken.as_view())
]
