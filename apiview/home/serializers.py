from rest_framework import serializers
from .models import *

# class StudentSerializer(serializers.Serializer):
#    name =serializers.CharField(max_length=100)
#    age = serializers.IntegerField(default=18)
#    city =serializers.CharField(max_length=100)

class StudentSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Student
    fields ='__all__'
    # exclude = ['age']
    



  def validate(self, data):
       if data.get("age") is not None and data["age"] < 18:
            raise serializers.ValidationError({"error": "Age cannot be less than 18"})
          
       if data['name']:
         for n in data['name']:
           if n.isdigit():
             raise serializers.ValidationError({"error": "name can't be numeric"})
             
        
       return data
     
class CategorySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Category
    fields ='__all__'
    # exclude = ['age']
    
class BookSerializer(serializers.ModelSerializer):
  category =CategorySerializer()
  class Meta:
    model = Book
    fields ='__all__'
    # exclude = ['age']
