"""weatherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from weather import views

urlpatterns = [
    path('', views.home),
    path('weather/', views.new_search),
    path('admin/', admin.site.urls),
    path('weather/new_search', views.new_search),
    path('weather/<str:city>', views.city_search),
    path('main/', views.main),
    path('main/new_search', views.new_search),
    path('main/add_to_favorite/<str:city>', views.add_to_favorite),
    path('main/delete_favorite/<int:id>', views.delete_favorite),

]
