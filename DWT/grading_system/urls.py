from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('add-user/', UserCreate.as_view(), name="add-user"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', UserLogout.as_view(), name="logout"),
    path('user-list/', UserList.as_view(), name="user-list"),  # get method to get all the user
    path('get-user/<int:pk>/', UserRetreive.as_view(), name="get-user"),
    path('update-user/<int:pk>/', UserUpdate.as_view(), name="update-user"),  # update the user by id
    path('delete-user/<int:pk>/', UserDelete.as_view(), name="delete-user"),  # delete the user by id
    path('add-class/', ClassCreate.as_view(), name="add-class"),
    path('class-list/', ClassList.as_view(), name="class-list"),
    path('update-class/<int:pk>/', ClassUpdate.as_view(), name="update-class"),
    path('delete-class/<int:pk>/', ClassDestroy.as_view(), name="delete-class"),
    path('add-subject/', SubjectCreate.as_view(), name="add-subject"),
    path('subject-list/', SubjectList.as_view(), name="subject-list"),
    path('update-subject/<int:pk>/', SubjectUpdate.as_view(), name="update-subject"),
    path('delete-subject/<int:pk>/', SubjectDestroy.as_view(), name="delete-subject"),
    path('add-test/', TestCreate.as_view(), name="add-test"),
    path('test-list/', TestList.as_view(), name="test-list"),
    path('update-test/<int:pk>/', TestUpdate.as_view(), name="update-test"),
    path('delete-test/<int:pk>/', TestDestroy.as_view(), name="delete-test"),
    path('add-assignedpupil/', AssignedPupilCreate.as_view(), name="add-assignedpupil"),
    path('assignedpuptil-list/', AssignedPupilList.as_view(), name="assignedpupil-list"),
    path('update-assignedpupil/<int:pk>/', AssignedPupilUpdate.as_view(), name="update-assignedpupil"),
    path('delete-assignedpupil/<int:pk>/', AssignedPupilDestroy.as_view(), name="delete-assignedpupil"),
    path('get-all-student', StudentList.as_view(), name="get-all-student"),
    path('get-all-teacher', TeacherList.as_view(), name="get-all-teacher"),
    path('add-grade/', GradeCreate.as_view(), name="add-grade"),
    path('grade-list/', GradeList.as_view(), name="grade-list"),
    path('update-grade/<int:pk>/', GradeUpdate.as_view(), name="update-grade"),
    path('delete-grade/<int:pk>/', GradeDestroy.as_view(), name="delete-grade"),
    path('file-upload-csv', FileUploadAPIView.as_view(), name="file-upload-csv"),
    path('admindashboard', views.adminview, name="admindashboard"),
    path('studentdashboard', StudentView.as_view(), name="studentdashboard"),
    path('teacherdashboard', TeacherView.as_view(), name="teacherdashboard"),
    path('home', HomePageView.as_view(), name='home'),

]
