from django.urls import include, path

from .views import *

urlpatterns = [
    path('', UserListView.as_view()),
    path('signup/student/', StudentSignUpView.as_view()),
    path('signup/teacher/', TeacherSignUpView.as_view()),
    # path('accounts/signup/teacher/', views.TeacherSignUpView),
]