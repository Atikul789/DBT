from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('createuser/', UserCreate.as_view(), name="createuser"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', UserLogout.as_view(), name="logout"),
    path('userlist/', UserList.as_view(), name="userlist"),  # get method to get all the user
    path('retreiveuser/<int:pk>/',UserRetreive.as_view(), name="retreiveuser"),
    path('updateuser/<int:pk>/', UserUpdate.as_view(), name="userupdate"),  # update the user by id
    path('deleteuser/<int:pk>/', UserDelete.as_view(), name="userdelete"),  # delete the user by id
    path('createclass/', ClassCreate.as_view(), name="createclass"),
    path('classlist/', ClassList.as_view(), name="classlist"),
    path('updateclass/<int:pk>/', ClassUpdate.as_view(), name="updateclass"),
    path('deleteclass/<int:pk>/', ClassDestroy.as_view(), name="deleteclass"),
    path('createsubject/', SubjectCreate.as_view(), name="createsubject"),
    path('subjectlist/', SubjectList.as_view(), name="subjectlist"),
    path('updatesubject/<int:pk>/', SubjectUpdate.as_view(), name="updatesubject"),
    path('deletesubject/<int:pk>/', SubjectDestroy.as_view(), name="deletesubject"),
    path('createtest/', TestCreate.as_view(), name="createtest"),
    path('testlist/', TestList.as_view(), name="testlist"),
    path('updatetest/<int:pk>/', TestUpdate.as_view(), name="updatetest"),
    path('deletetest/<int:pk>/', TestDestroy.as_view(), name="deletetest"),
    path('createassignedpupil/', AssignedPupilCreate.as_view(), name="createassignedpupil"),
    path('assignedpuptillist/', AssignedPupilList.as_view(), name="assignedpupillist"),
    path('updateassignedpupil/<int:pk>/', AssignedPupilUpdate.as_view(), name="updateassignedpupil"),
    path('deleteassignedpupil/<int:pk>/', AssignedPupilDestroy.as_view(), name="deleteassignedpupil"),
    path('home', HomePageView.as_view(), name='home'),

]
