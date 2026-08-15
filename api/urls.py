from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('employee',views.EmployeesViewSet,basename='employee')

urlpatterns = [
    path('students/',views.studentsView),
path("students/<int:id>/", views.studentDetail),


# path("employee/",views.Employees.as_view()),
# path("employee/<int:pk>/",views.EmployeesDtail.as_view())

path('',include(router.urls))
]
