from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create', views.post_create, name='post_create'),
    path('additional', views.course_additional, name='course_additional')
    # 前面是網址部分，最後是模板要用的url
]