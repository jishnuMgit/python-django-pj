from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentsView),
path("students/<int:id>/", views.studentDetail),


path("employee/",views.Employees.as_view()),
path("employee/<int:pk>/",views.EmployeesDtail.as_view())
]
