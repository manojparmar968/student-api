from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import traceback
from .token import get_access_token
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from django.contrib.auth import authenticate, login
import re
from common_app.models import Account
from oauth2_provider.models import Application , RefreshToken
from .function import *
from django.db.models import Q
import datetime
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
from .permission import IsUserOnly
import json
from mobile_webapp.models import *

# sign up using jwt

class SignupViewset(viewsets.ViewSet):
    def create(self, request):
        print('request.POST',request.POST)
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            account_type = request.data.get('account_type')

            if not re.search(r'\w+@\w+',email if email else "not a email"):
                raise Exception("email id is not valid")
            if password and len(password)<6:
                raise Exception("password should be atleast 6 charater")
            if email and password:
                if not first_name:
                    raise Exception('please enter first name')
                if not last_name:
                    raise Exception('please enter last name')
                if is_email_exist(email):
                    raise Exception('email already exist')
                account_obj = Account.objects.create(email=email,name= str(first_name)+" "+str(last_name),account_type=account_type)
                account_obj.set_password(password)
                account_obj.save()
                Application.objects.get_or_create(user=account_obj,client_type=Application.CLIENT_CONFIDENTIAL,authorization_grant_type=Application.GRANT_PASSWORD)
                token = get_access_token(account_obj)
                return Response({'token': token,"message":"Register Successfully","success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK) 

# Rest password using Jwt
class ResetPasswordViewset(viewsets.ViewSet):
    permission_classes = [TokenHasReadWriteScope]

    def create(self, request):
        try:
            password = request.data.get('password')
            if password and len(password)<6:
                raise Exception("password should be atleast 6 charater")
            user_obj = Account.objects.get(email=request.user.email)
            user_obj.set_password(password)
            user_obj.save()
            return Response({'message':"password reset successfully","success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)

# Add Student Successfully 

class AddStudent(viewsets.ViewSet):
    permission_classes = [TokenHasReadWriteScope,IsUserOnly]
    def create(self, request):
        try:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            DOB = request.data.get('DOB')
            email = request.data.get('email')
            mobile_number = request.data.get('mobile_number')
            address = request.data.get('address')
            student = Students.objects.create(name= str(first_name)+" "+str(last_name),DOB=DOB,email=email,mobile_number=mobile_number,address=address,)
            return Response({'message':"Student add successfully","success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)

# Get Students Data

class StudentViewset(viewsets.ViewSet):
    permission_classes = [TokenHasReadWriteScope,IsUserOnly]

    def list(self, request):
        try:
            student_list = [{"id":student_obj.id,"name":student_obj.name,"DOB":student_obj.DOB,"mobile_number":student_obj.mobile_number,"email":student_obj.email,'address':student_obj.address } 
            for student_obj in Students.objects.all()]
            return Response({"data":student_list,"success":True},status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)
