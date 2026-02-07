from rest_framework import serializers
from . models import Student_API

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_API
        fields = "__all__"