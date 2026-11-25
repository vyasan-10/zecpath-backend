from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .services import create_job, create_user, get_all_jobs, get_all_users
from .utils import api_response


def home_api(request):
  return JsonResponse({'message': 'Hello Zecpath Backend'})


class UserTestAPI(APIView):

  def get(self, request):
    users = get_all_users()
    return api_response(
        data=users, message='Users retrieved successfully'
    )

  def post(self, request):
    user = create_user(request.data)
    return api_response(
        data=user,
        message='User created successfully',
        status_code=status.HTTP_201_CREATED,
    )


class JobListCreateAPI(APIView):

  def get(self, request):
    jobs = get_all_jobs()
    return api_response(data=jobs, message='Jobs retrieved successfully')

  def post(self, request):
    job = create_job(request.data)
    return api_response(
        data=job,
        message='Job created successfully',
        status_code=status.HTTP_201_CREATED,
    )