
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('studentdata', views.studentdataapi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(router.urls)),
    path('home' , views.displaydata),
    path('edit/<int:pk>',views.studentupdate.as_view()),
    path('post',views.postapi,name="postapi"),

]
