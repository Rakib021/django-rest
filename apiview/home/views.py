from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def home(request):
  student_obj = Student.objects.all()
  serializer = StudentSerializer(student_obj,many=True)
  return Response({"status":200,"message": serializer.data})

@api_view(['POST'])
def data_post(request):
   data = request.data

   serializer = StudentSerializer(data= request.data)
   if not serializer.is_valid():
     return Response({"status":403,"payload": serializer.errors,"msg":"something went wrong"})
      
   serializer.save()
      
   return Response({"status":200,"payload": serializer.data,"msg":"sent data"})
 
@api_view(['PATCH'])
def data_update(request,id):
  try:
    stu_obj = Student.objects.get(id=id)
    serializer = StudentSerializer(stu_obj,data= request.data,partial=True)
    if not serializer.is_valid():
      return Response({"status":403,"payload": serializer.errors,"msg":"something went wrong"})
        
    serializer.save()
        
    return Response({"status":200,"payload": serializer.data,"msg":"data updated"})
  
  except Exception as e:
    return Response({"status":403,"msg":"invalid id "})
  
@api_view(['DELETE'])
def data_delete(request,id):
  try:
    stu_obj = Student.objects.get(id=id)
    stu_obj.delete()
    return Response({"status":200,"msg":"Data deleted "})
    
  except Exception as e:
    return Response({"status":403,"msg":"invalid id "})
    
@api_view(['GET'])
def book_detail(request):
  book_obj = Book.objects.all()
  serializer = BookSerializer(book_obj,many=True)
  return Response({"status":200,"message": serializer.data})
    
    