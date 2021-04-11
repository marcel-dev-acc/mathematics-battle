from django.db.models.fields import NOT_PROVIDED
from django.http import JsonResponse
import logging
import traceback
from datetime import datetime
import json
import uuid
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .models import Session
from .models import Question

logger = logging.getLogger(__name__)

# Create your views here.
def api_status(request) -> JsonResponse:
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


@csrf_exempt
def create_session(request) -> JsonResponse:
    """Method to create new sessions."""
    try:
        if request.method == 'POST':
            session_id = uuid.uuid4()
            session = Session(
                uuid=session_id,
            ).save()
            response = {
                'status': 'ok',
                'message': 'Request successful',
                'data': {
                    'session_id': session_id,
                },                
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


def get_sessions(request) -> JsonResponse:
    """Method to get sessions."""
    try:
        if request.method == 'GET':
            sessions_list = []
            sessions = Session.objects.all()
            for session in sessions:
                sessions_list.append(session.uuid)
            response = {
                'status': 'ok',
                'message': 'Request successful',
                'data': sessions_list,
            }
            return JsonResponse(response, safe=False, status=200)
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

@csrf_exempt
def add_user_to_session(request, session_id) -> JsonResponse:
    """Method to add a user to a session."""
    try:
        print(request.method)
        if request.method == 'PUT':
            # request_payload = json.loads(
            #     request.body.decode('latin1')
            # )
            request_payload = json.loads(
                request.body.decode('latin1')
            )

            username = request_payload.get('username')
            if not username:
                response = {
                    'status': 'error',
                    'message': 'Please provide a username'
                }
                return JsonResponse(response, status=400)

            session = Session.objects.filter(uuid=session_id).first()
            if not session:
                response = {
                    'status': 'error',
                    'message': 'Session not found'
                }
                return JsonResponse(response, status=401)

            added_user = User(
                username=username,
                session=session
            ).save()

            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a PUT request'
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


def get_new_problem(request) -> JsonResponse:
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


@csrf_exempt
def submit_problem_solution(request) -> JsonResponse:
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