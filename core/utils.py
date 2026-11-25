from rest_framework import status
from rest_framework.response import Response


def api_response(
    data=None, message="Success", status_code=status.HTTP_200_OK
):
  return Response(
      {
          "status": "success" if status_code < 400 else "error",
          "message": message,
          "data": data,
      },
      status=status_code,
  )