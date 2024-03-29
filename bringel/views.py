from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from client.tasks import fibonacci, factorial, task_with_delay, get_name_rr, add  # noqa E501
import time
from drf_yasg.utils import swagger_auto_schema
import logging

logger = logging.getLogger(__name__)


@swagger_auto_schema(operation_id='i can change name here',
                     tags=['welcome'],
                     method='get')
@api_view(["GET"])
def welcome(request):
    """
    Home page
    """
    content = {"message": "Bem vindo à Bringel Store!"}
    logger.debug('DEGUG CRITICAL Usuário acessou a página inicial')
    logger.warning('WARNING CRITICAL Usuário acessou a página inicial')
    logger.error('ERROR Usuário acessou a página inicial')
    logger.info('INFO Usuário acessou a página inicial')
    logger.critical('CRITICAL Usuário acessou a página inicial')
    return JsonResponse(content)


def error(request):
    content = {"error": "Rota inválida!"}
    return JsonResponse(content)


class CeleryAPIListView(APIView):
    """
    Example to use:
    ?m=68&n=46
    """

    def get(self, request):

        n = int(request.query_params.get('n', 10))  # Default n is 10
        fibonacci_result = fibonacci.delay(n).get()

        m = int(request.query_params.get('m', 5))  # Default m is 5
        factorial_result = factorial.delay(m).get()

        task_result = task_with_delay.delay().get()

        get_name_rr_result = get_name_rr.delay().get()

        response_data = {
            'fibonacci_result': fibonacci_result,
            'factorial_result': factorial_result,
            'task_with_delay_result': task_result,
            'get_name_rr_result': get_name_rr_result,
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        # Get request data if needed
        arg1 = request.data.get('arg1', 10)
        arg2 = request.data.get('arg2', 5)

        # Call the Celery task
        result = add.delay(arg1, arg2)
        # Get the task result
        while not result.ready():
            print("Tarefa rodando...")
            time.sleep(1)

        response_data = {'task_id': result.get()}

        return Response(response_data, status=status.HTTP_202_ACCEPTED)
