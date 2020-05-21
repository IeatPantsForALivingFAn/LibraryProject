from rest_framework import serializers
from .models import Student
#serializer classes

class StudentSerializer(serializers.ModelSerializer):
    user = serializer.CharField(source='user.username')

    class Meta:
        model = Student
        fields = ['id','user','name','roll_no','branch','sem']