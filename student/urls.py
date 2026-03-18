from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list),
    path('enroll/', views.enroll_course),
]
