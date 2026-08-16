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

path('',include(router.urls)),

path('blogs/',views.BlogViews.as_view()),
path('comments/',views.CommentView.as_view()),
path(
    'blogs/<int:pk>/',
    views.BlogDetailView.as_view()
),
path(
    'comments/<int:pk>/',
    views.CommentDetailView.as_view()
),
]
