from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import (
    course as Course,
    examAttempt as QExam, 
    techingAssistant as TA, 
    research as Research,
    paper as Paper
    )


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['username', 'Questionnaire_For', 'Subject_Name', 'Subject_Code', 'Subject_Term_and_Year', 'Grade']

class QExamForm(ModelForm):
    class Meta:
        model = QExam
        fields = ['username', 'Questionnaire_For', 'Exam_Name', 'Attempt_Number', 'Grade']

class TeachingForm(ModelForm):
    class Meta:
        model = TA
        fields = ['username', 'Questionnaire_For', 'Subject_Name', 'Subject_Code', 'In_Which_Semester', 'Instructor_Name',
         'Responsibilities', 'Lecture_or_Presentation_Given', 'Area_of_Improvement']

class ResearchForm(ModelForm):
    class Meta:
        model = Research
        fields = ['username', 'Questionnaire_For', 'Topic', 'Proposal', 'Defense', 'Current_Academic_Advisor', 'Current_Research_Advisor']

class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ['Author', 'Questionnaire_For', 'Title', 'Venue', 'Status_of_Paper', 'Coauthor']