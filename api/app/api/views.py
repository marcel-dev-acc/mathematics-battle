from django.http import JsonResponse
import logging
import traceback
from datetime import datetime
import json

logger = logging.getLogger(__name__)

# Create your views here.
def api_status(request):
    """Method to check if the status is live."""
    try:
        if request.method == 'GET':
            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a GET request'
            }
            return JsonResponse(response, status=400)
    except Exception as ex:
        logger.error(
            'DateTime: {}, Exception: {}, Trace: {} '.format(
                datetime.now(),
                ex,
                traceback.format_exc()
            )
        )
        response = {
            'status': 'error',
            'message': 'Unexpected error'
        }
        return JsonResponse(response, status=500)



def create_session(request):
    """Method to create new sessions."""
    try:
        if request.method == 'POST':
            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a POST request'
            }
            return JsonResponse(response, status=400)
    except Exception as ex:
        logger.error(
            'DateTime: {}, Exception: {}, Trace: {} '.format(
                datetime.now(),
                ex,
                traceback.format_exc()
            )
        )
        response = {
            'status': 'error',
            'message': 'Unexpected error'
        }
        return JsonResponse(response, status=500)


def get_sessions(request):
    """Method to get sessions."""
    try:
        if request.method == 'GET':
            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a GET request'
            }
            return JsonResponse(response, status=400)
    except Exception as ex:
        logger.error(
            'DateTime: {}, Exception: {}, Trace: {} '.format(
                datetime.now(),
                ex,
                traceback.format_exc()
            )
        )
        response = {
            'status': 'error',
            'message': 'Unexpected error'
        }
        return JsonResponse(response, status=500)


def add_user_to_session(request, session_id):
    """Method to add a user to a session."""
    try:
        if request.method == 'PUT':
            request_payload = json.loads(
                request.body.decode('latin1')
            )
            username = request_payload.get('username')
            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a GET request'
            }
            return JsonResponse(response, status=400)
    except Exception as ex:
        logger.error(
            'DateTime: {}, Exception: {}, Trace: {} '.format(
                datetime.now(),
                ex,
                traceback.format_exc()
            )
        )
        response = {
            'status': 'error',
            'message': 'Unexpected error'
        }
        return JsonResponse(response, status=500)


def get_new_problem(request):
    """Method to get a new problem to solve."""
    try:
        if request.method == 'GET':
            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a GET request'
            }
            return JsonResponse(response, status=400)
    except Exception as ex:
        logger.error(
            'DateTime: {}, Exception: {}, Trace: {} '.format(
                datetime.now(),
                ex,
                traceback.format_exc()
            )
        )
        response = {
            'status': 'error',
            'message': 'Unexpected error'
        }
        return JsonResponse(response, status=500)



def submit_problem_solution(request):
    """Method to submit a solution to a problem."""   
    try:
        if request.method == 'POST':
            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a POST request'
            }
            return JsonResponse(response, status=400)
    except Exception as ex:
        logger.error(
            'DateTime: {}, Exception: {}, Trace: {} '.format(
                datetime.now(),
                ex,
                traceback.format_exc()
            )
        )
        response = {
            'status': 'error',
            'message': 'Unexpected error'
        }
        return JsonResponse(response, status=500)