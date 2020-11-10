from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StudentSerializer, TeacherSerializer, GradeSerializer
from .models import Student, Teacher, Grade
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        if request.GET.get("nama"):
            found_students = Student.objects.filter(nama__icontains=request.GET.get("nama"))
            found_students_sr = StudentSerializer(found_students, many=True)
            return JsonResponse(found_students_sr.data, safe=False)
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        grade = Grade.objects.get(pk=student_data['grade_id']) 
        student_data['grade'] = grade.id
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    # find tutorial by pk (id)
    try:
        tutorial = Student.objects.get(pk=pk) 
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': 
        student_serializer = StudentSerializer(tutorial) 
        return JsonResponse(student_serializer.data) 

    elif request.method == 'PUT': 
        student = JSONParser().parse(request) 
        student_serializer = StudentSerializer(tutorial, data=student) 
        if student_serializer.is_valid(): 
            student_serializer.save() 
            return JsonResponse(student_serializer.data) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        Student.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'})

@api_view(['GET'])
def student_detail(request, query):
    print(query)
    # try:
    #     tutorial = Student.objects.filter(pk=pk) 
    # except Tutorial.DoesNotExist:
    #     return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # if request.method == 'GET': 
    #     student_serializer = StudentSerializer(tutorial) 
    return JsonResponse("test")

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class GradeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Grade.objects.all().order_by('id')
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
