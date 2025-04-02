from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


class CustomResponse(Response):

    def __init__(self, data=None, status=200, error=None, message="", **kwargs):
        standard_response = {
            "status": "success" if status in range(200, 300) else "error",
            "status_code": status,
            "error": error or [],
            "data": data or {},
            "message": message
        }
        super().__init__(data=standard_response, status=status, **kwargs)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        errors = []

        if "detail" in response.data:
            errors.append(str(response.data["detail"]))
        elif isinstance(response.data, list):
            for error in response.data:
                errors.append(str(error))
        else:
            for field, error in response.data.items():
                errors.append(f"{field}: {error[0] if len(error) == 1 else error}")

        custom_response = CustomResponse(error=errors, status=response.status_code)
        response = custom_response
    elif isinstance(exc, Exception):
        status_code = getattr(exc, 'status_code', status.HTTP_400_BAD_REQUEST)
        response = CustomResponse(error=str(exc), status=status_code)

    return response
