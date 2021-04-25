from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mobile_webapp.views import *

router = DefaultRouter()
router.register(r'v1/signup', SignupViewset, basename='SignupViewset')
router.register(r'v1/reset-password', ResetPasswordViewset, basename='ResetPasswordViewset')
router.register(r'v1/Add-Student', AddStudent, basename='AddStudent')
router.register(r'v1/Student-View', StudentViewset, basename='StudentViewset')

urlpatterns = [
    path('', include(router.urls)),
]
