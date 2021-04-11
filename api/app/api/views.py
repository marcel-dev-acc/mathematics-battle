from django.db.models.fields import NOT_PROVIDED
from django.http import JsonResponse
import logging
import traceback
from datetime import datetime
import json
import uuid
import random
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
            )
            session.save()
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
def add_user_to_session(request, session_id=None) -> JsonResponse:
    """Method to add a user to a session."""
    try:
        print(request.method)
        if request.method == 'PUT':
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
            )
            added_user.save()

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


def get_new_problem(request, session_id=None, username=None) -> JsonResponse:
    """Method to get a new problem to solve."""
    try:
        if request.method == 'GET':
            session = Session.objects.filter(uuid=session_id).first()
            if not session:
                response = {
                    'status': 'error',
                    'message': 'Session not found'
                }
                return JsonResponse(response, status=404)

            user = User.objects.filter(username=username).first()
            if not user:
                response = {
                    'status': 'error',
                    'message': 'User not found'
                }
                return JsonResponse(response, status=404)

            number_1 = int(random.random() * 100)
            number_2 = int(random.random() * 100)
            list_of_operators = ['+', '-']
            operator_index = int(random.random() * len(list_of_operators)) - 1
            string_question = '{} {} {}'.format(
                number_1,
                list_of_operators[operator_index],
                number_2
            )
            problem_solution = str(eval(string_question))
            problem = Question(
                question=string_question,
                answer=problem_solution,
                correct=False,
                session=session,
                user=user
            )
            problem.save()

            response = {
                'status': 'ok',
                'message': 'Request successful',
                'data': {
                    'question_id': problem.id,
                    'problem': string_question,
                }
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
def submit_problem_solution(request, session_id=None, username=None) -> JsonResponse:
    """Method to submit a solution to a problem."""   
    try:
        if request.method == 'POST':
            request_payload = json.loads(
                request.body.decode('latin1')
            )

            try:
                problem_id = int(request_payload.get('problem_id'))
            except ValueError as ex:
                response = {
                    'status': 'error',
                    'message': 'Please provide a valid problem ID'
                }
                return JsonResponse(response, status=400)
            if not problem_id:
                response = {
                    'status': 'error',
                    'message': 'Please provide a problem ID'
                }
                return JsonResponse(response, status=400)

            answer = str(request_payload.get('answer'))
            if not answer:
                response = {
                    'status': 'error',
                    'message': 'Please provide a solution'
                }
                return JsonResponse(response, status=400)

            # TODO include validation for problem session.id
            # TODO include validation for problem user.username

            problem = Question.objects.filter(id=problem_id).first()
            if problem.answer == answer:
                problem.correct = True
                problem.save()

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