from rest_framework import serializers
from .models import Job, User


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'name', 'email', 'role', 'created_at']


class JobSerializer(serializers.ModelSerializer):

  class Meta:
    model = Job
    fields = [
        'id',
        'employer',
        'title',
        'description',
        'skills_required',
        'location',
        'salary_range',
        'is_open',
        'created_at',
    ]