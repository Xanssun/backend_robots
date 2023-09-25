from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from robots.forms import RobotForm

from .models import Robot


@method_decorator(csrf_exempt, name='dispatch')
class RobotView(View):

    def get(self, request):
        robots = Robot.objects.all()
        robots_serialized_data = serialize('python', robots)
        data = {
            'robots': robots_serialized_data,
        }
        return JsonResponse(data)
    
    def post(self, request):
        if request.method == "POST":
            post = json.loads(request.body)
            form = RobotForm(post)

            if form.is_valid():
                form.save()
                data = {
                    'message': 'Новый робот был создан'
                }
            else:
                data = {
                    'error': 'Неверные данные'
                }
        else:
            data = {
                'error': 'Неверный метод запроса'
            }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class RobotUpdateDeleteView(View):

    def put(self, request, robot_id):
        if request.method == "PUT":
            robot = get_object_or_404(Robot, pk=robot_id)
            put_data = json.loads(request.body)
            form = RobotForm(put_data, instance=robot)
            
            if form.is_valid():
                form.save()
                data = {
                    'message': 'Робот успешно обновлен'
                }
            else:
                data = {
                    'error': 'Неверные данные'
                }
        else:
            data = {
                'error': 'Неверный метод запроса'
            }
        
        return JsonResponse(data)
    
    def delete(self, request, robot_id):
        if request.method == "DELETE":
            robot = get_object_or_404(Robot, pk=robot_id)
            robot.delete()
            data = {
                'message': 'Робот успешно удален'
            }
        else:
            data = {
                'error': 'Неверный метод запроса'
            }
        return JsonResponse(data)