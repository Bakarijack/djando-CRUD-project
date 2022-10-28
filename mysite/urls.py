"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp import views as myapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flower/<slug:slug>/',myapp_views.detail, name='detail'), #<> are used to capture the url values
    path('tags/<slug:slug>/',myapp_views.tags,name='tags'),
    path('flower/',myapp_views.create, name="create"),
    path('flower/edit/<int:pk>/',myapp_views.edit, name="edit"),
    path('',myapp_views.index, name='index'),
]
