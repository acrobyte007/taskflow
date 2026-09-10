from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse


def hello(request):
    return JsonResponse({
        "message": "Hello from Django!"
    })

def task_list(request):
    tasks = [
        {"id": 1, "title": "Learn Django", "completed": False},
        {"id": 2, "title": "Build SaaS", "completed": False},
        {"id": 3, "title": "Learn Django REST Framework", "completed": False},
    ]

    return JsonResponse({
        "tasks": tasks
    })


def task_detail(request, task_id):
    tasks = [
        {"id": 1, "title": "Learn Django", "completed": False},
        {"id": 2, "title": "Build SaaS", "completed": False},
        {"id": 3, "title": "Learn DRF", "completed": False},
    ]

    for task in tasks:
        if task["id"] == task_id:
            return JsonResponse(task)

    return JsonResponse(
        {"error": "Task not found"},
        status=404
    )


def task_create(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed"},
            status=405
        )

    data = json.loads(request.body)

    title = data.get("title")
    completed = data.get("completed", False)

    task = {
        "id": 4,
        "title": title,
        "completed": completed
    }

    return JsonResponse(task, status=201)


def create_task_page(request):

    if request.method == "POST":
        title = request.POST.get("title")

        task = {
            "id": 4,
            "title": title,
            "completed": False
        }

        return JsonResponse(task, status=201)

    return render(request, "tasks/create.html")