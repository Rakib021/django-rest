from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer,UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.


class UserView(APIView):
  
  def post(self,request):
    serializer = UserSerializer(data = request.data)
    if not serializer.is_valid():
        return Response({"status":403,"payload": serializer.errors,"msg":"something went wrong"})
          
    serializer.save()
    user = User.objects.get(username = serializer.data['username'])
    # token, _ = Token.objects.get_or_create(user=user)
    refresh = RefreshToken.for_user(user)

          
    return Response({"status":200,"payload": serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        "msg":"Registration complete"})
    
    
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self,request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj,many=True)
    return Response({"status":200,"message": serializer.data})
  
  def post(self,request):
    serializer = StudentSerializer(data= request.data)
    if not serializer.is_valid():
        return Response({"status":403,"payload": serializer.errors,"msg":"something went wrong"})
          
    serializer.save()
          
    return Response({"status":200,"payload": serializer.data,"msg":"sent data"})
  
  def patch(self,request):
     try:
      stu_obj = Student.objects.get(id=request.data['id'])
      serializer = StudentSerializer(stu_obj,data= request.data)
      if not serializer.is_valid():
         return Response({"status":403,"errors": serializer.errors,"msg":"something went wrong"})
        
      serializer.save()
        
      return Response({"status":200,"payload": serializer.data,"msg":"data updated"})
  
     except Exception as e:
        return Response({"status":403,"msg":"invalid id "})
    
  def delete(self, request):
    try:
       id = request.GET.get('id')
       stu_obj = Student.objects.get(id=id)
       stu_obj.delete()
       return Response({"status":200,"msg":"Data deleted "})
    
    except Exception as e:
       return Response({"status":403,"msg":"invalid id "})
