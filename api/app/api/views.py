from django.http import JsonResponse
import logging
import traceback
from datetime import datetime

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# Create your views here.
def api_status(request):
    try:
        if request.method == 'GET':
            response = {
                'status': 'ok',
                'message': 'Request successful'
            }
            return JsonResponse(response, 200)
        else:
            response = {
                'status': 'error',
                'message': 'Not a GET request'
            }
            return JsonResponse(response, 400)
    except Exception as ex:
        logging.error(
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
        return JsonResponse(response, 500)