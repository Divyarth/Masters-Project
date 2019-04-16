from django.urls import path
from . import views
from .views import (
    PaperListView,
    PaperDetailView,
    PaperCreateView,
    PaperUpdateView,
    PaperDeleteView,
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)
urlpatterns = [
    path('', views.home, name='questionnaire-home'),
    path('questionnaire/', views.questionnaire, name='questionnaire-form'),
    path('questionnaire/step1', views.saveCourses, name='questionnaire-form-courses'),
    path('questionnaire/step2', views.saveQExams, name='questionnaire-form-qexams'),
    path('questionnaire/step3', views.saveTA, name='questionnaire-form-teaching'),
    path('questionnaire/step4', views.saveResearch, name='questionnaire-form-research'),
    path('questionnaire/step3', views.savePapers, name='questionnaire-form-paper'),
    path('paper/', PaperListView.as_view(), name='paper-all'),
    path('paper/all/', PaperListView.as_view(), name='paper-all'),
    path('paper/<int:pk>/', PaperDetailView.as_view(), name='paper-detail'),
    path('paper/new/', PaperCreateView.as_view(), name='paper-create'),
    path('paper/<int:pk>/update/', PaperUpdateView.as_view(), name='paper-update'),
    path('paper/<int:pk>/delete/', PaperDeleteView.as_view(), name='paper-delete'),
    path('course/all/', CourseListView.as_view(), name='course-all'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/new/', CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]
