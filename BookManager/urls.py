"""
URL configuration for BookManager project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from BookManager.settings import MEDIA_ROOT , MEDIA_URL
from Books.views import user_login , user_logout , book_create ,dashboard , book_list, book_delete,book_update, book_detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_login, name='user_login'),
    path('list/', book_list, name='book_list'),
    path('add/', book_create, name='book_create'),
    path('d/', dashboard, name='dashboard'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('edit/<int:pk>/',book_update, name='book_update'),
    path('delete/<int:pk>/', book_delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

