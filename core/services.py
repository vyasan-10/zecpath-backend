from .models import Job, User
from .serializers import JobSerializer, UserSerializer


def get_all_users():
    users = User.objects.all().order_by('-created_at')
    return UserSerializer(users, many=True).data


def create_user(data):
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def get_all_jobs():
    jobs = Job.objects.select_related('employer').filter(is_open=True)
    return JobSerializer(jobs, many=True).data


def create_job(data):
    serializer = JobSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data