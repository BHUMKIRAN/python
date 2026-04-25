from django.http import JsonResponse
from .models import Student

def student_list(request):
    students = Student.objects.all()
    data = []
    for student in students:
        data.append({
            'name': student.name,
            'age': student.age,
            'email': student.email
        })
    return JsonResponse(data, safe=False)