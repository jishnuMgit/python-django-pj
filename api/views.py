from django.http import JsonResponse
from students.models import Students
from .serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def studentsView(request):
    # students = Students.objects.all()
    # oneStudent = Students.objects.values().get(id=1)

    # student_list = list(students.values())

    # return JsonResponse({
    #     "students": student_list,
    #     "oneStudent": oneStudent
    # })
    if request.method=='GET':
        students =Students.objects.all()
        serializer=StudentsSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)