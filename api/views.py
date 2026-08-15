from django.http import JsonResponse
from students.models import Students
from .serializers import StudentsSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
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
    elif request.method=='POST':
        serializer=StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def studentDetail(request, id):

    try:
        student = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return Response(
            {"error": "Student not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = StudentsSerializer(student)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'PUT':
        serializer = StudentsSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class Employees(APIView):
#     def get(self,request):
#         employees=Employee.objects.all()
#         serializer=EmployeeSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()    
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


# class EmployeesDtail(APIView):
#     def get_object(self,id):  
#         try:
#             employee=Employee.objects.get(id=id)
#             return employee 
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self,requst,id):
#         employee=self.get_object(id)    
#         serializer=EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def put(self,request,id) :
#         employee=self.get_object(id)
#         serializer=EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,id):
#         employee=self.get_object(id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

        
"""
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 

    def get(self,request) :
        return self.list(request)  
    def post(self,request):
        return self.create(request)

class EmployeesDtail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)

    
 """

#Generics
class Employees(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer





class EmployeesDtail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'

"""
class EmployeesViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Employee.objects.all()
        serializer=EmployeeSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        employee=get_object_or_404(Employee,pk=pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def update(self,request,pk):
         
         employee=get_object_or_404(Employee,pk=pk)
         serializer=EmployeeSerializer(employee,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_200_OK)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
         employee=get_object_or_404(Employee,pk=pk)
         employee.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


         """

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer