from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from todo_app.models import Todo
from todo_app.serializers import TodoSerializer

# Create your views here.
@csrf_exempt
def todoApi(request, id = 0):
    if request.method == 'GET':
        todos = Todo.objects.all()
        todos_serilizer = TodoSerializer(todos, many=True)
        return JsonResponse(todos_serilizer.data, safe=False)

    elif request.method == 'POST':
        todo_data = JSONParser().parse(request)
        todo_serilizer = TodoSerializer(data=todo_data)
        if todo_serilizer.is_valid():
            todo_serilizer.save()
            return JsonResponse("Todo created successfully", safe=False)
        return JsonResponse("Todo creation failed", safe=False)

    elif request.method == 'PUT':
        todo_data = JSONParser().parse(request)
        todo = Todo.objects.get(TodoId=todo_data['TodoId'])
        todo_serilizer = TodoSerializer(todo, data=todo_data)
        if todo_serilizer.is_valid():
            todo_serilizer.save()
            return JsonResponse("Todo updated successfully", safe=False)
        return JsonResponse("Todo update failed", safe=False)

    elif request.method == 'DELETE':
        todo = Todo.objects.get(TodoId=id)
        todo.delete()
        return JsonResponse("Todo deleted successfully", safe=False)