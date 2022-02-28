"""B6_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from book import views
print("in urls.py")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name ="homepage"),
    path('show-all-books/',views.show_all_books, name= "show_all_books"),
    path('edit/<int:id>/', views.edit_data, name="edit"),
    path('delete/<int:id>/',views.delete_data, name="delete"),
    path('form-home/', views.form_home, name ="form_home"),
]    


urlpatterns +=[
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]
urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls'))
]     