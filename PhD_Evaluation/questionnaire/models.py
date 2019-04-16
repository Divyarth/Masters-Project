from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class questionnaire(models.Model):
    isOpen = models.CharField(max_length=10)
    Questionnaire_For = models.CharField(max_length=100, unique=True)
    previous_term = models.ForeignKey('self', db_column="previous_term", on_delete=models.PROTECT, blank=True, null=True)
    status = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.datetime.now())
    end_date = models.DateField()
    def __str__(self):
        return self.Questionnaire_For


class qualifyingExam(models.Model):
    exam_Name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.exam_Name


class submissionTrack(models.Model):
    username = models.ForeignKey(User, db_column="username", on_delete=models.PROTECT)
    Questionnaire_For = models.ForeignKey(questionnaire, db_column="Questionnaire_For", on_delete=models.PROTECT)
    SAVE = 'Save'
    SUBMIT = 'Submit'
    choices = (
        (SAVE, 'Save'),
        (SUBMIT, 'Submit'),
    )
    saveSubmit = models.CharField(max_length=6, choices=choices)

    class Meta:
        unique_together = ('username', 'Questionnaire_For', 'saveSubmit',)

    def __str__(self):
        return str(self.username) + " " + str(self.Questionnaire_For) + " " + self.saveSubmit


class course(models.Model):
    username = models.ForeignKey(User, db_column="username", on_delete=models.PROTECT)
    Questionnaire_For = models.ForeignKey(questionnaire, db_column="Questionnaire_For", on_delete=models.PROTECT)
    Subject_Name = models.CharField(max_length=200)
    Subject_Code = models.CharField(max_length=50)
    Subject_Term_and_Year = models.CharField(max_length=50)
    Grade = models.CharField(max_length=20)

    class Meta:
        unique_together = ('username', 'Questionnaire_For', 'Subject_Name', 'Subject_Term_and_Year',)

    def __str__(self):
        return self.Subject_Code + " " + self.Subject_Term_and_Year


class examAttempt(models.Model):
    username = models.ForeignKey(User, db_column="username", on_delete=models.PROTECT)
    Questionnaire_For = models.ForeignKey(questionnaire, db_column="Questionnaire_For", on_delete=models.PROTECT)
    Exam_Name = models.ForeignKey(qualifyingExam, db_column="Exam_Name",
                                  on_delete=models.PROTECT)
    Attempt_Number = models.IntegerField(default="1", validators=[MaxValueValidator(4), MinValueValidator(1)])
    Grade = models.CharField(max_length=10)

    class Meta:
        unique_together = ('username', 'Exam_Name', 'Attempt_Number',)

    def __str__(self):
        return str(self.username) + " " + str(self.Exam_Name) + " " + str(self.Attempt_Number)


class techingAssistant(models.Model):
    username = models.ForeignKey(User, db_column="username", on_delete=models.PROTECT)
    Questionnaire_For = models.ForeignKey(questionnaire, db_column="Questionnaire_For", on_delete=models.PROTECT)
    Subject_Name = models.CharField(max_length=200)
    Subject_Code = models.CharField(max_length=50)
    In_Which_Semester = models.CharField(max_length=50)
    Instructor_Name = models.CharField(max_length=200)
    Responsibilities = models.TextField(max_length=5000)
    Lecture_or_Presentation_Given = models.TextField(max_length=5000)
    Area_of_Improvement = models.TextField(max_length=5000)

    class Meta:
        unique_together = ('username', 'Questionnaire_For', 'Subject_Name',)

    def __str__(self):
        return self.username + " " + self.Subject_Code + " " + self.In_Which_Semester


class paper(models.Model):
    Questionnaire_For = models.ForeignKey(questionnaire, db_column="Questionnaire_For", on_delete=models.PROTECT)
    Title = models.CharField(max_length=5000)
    Venue = models.CharField(max_length=1000)
    IP = 'In Progress'
    UR = 'Under Revision'
    PU = 'Published'
    status_choices = (
        (IP, IP),
        (UR, UR),
        (PU, PU),
    )
    Status_of_Paper = models.CharField(max_length=15, choices=status_choices, default=IP)
    Author = models.ForeignKey(User, db_column="Author", on_delete=models.PROTECT)
    Coauthor = models.TextField(max_length=5000)

    class Meta:
        unique_together = ('Author', 'Questionnaire_For', 'Title',)

    def __str__(self):
        return str(self.Author) + " " + str(self.Questionnaire_For) + " " + self.Title


class research(models.Model):
    username = models.ForeignKey(User, db_column="username", on_delete=models.PROTECT)
    Questionnaire_For = models.ForeignKey(questionnaire, db_column="Questionnaire_For", on_delete=models.PROTECT)
    Topic = models.CharField(max_length=5000, blank=True, null=True)
    Proposal = models.CharField(max_length=5000, blank=True, null=True)
    Defense = models.CharField(max_length=5000, blank=True, null=True)
    Current_Academic_Advisor = models.ForeignKey(User, db_column="Current_Academic_Advisor", on_delete=models.PROTECT, related_name='academic_advisor', blank=True, null=True)
    Current_Research_Advisor = models.ForeignKey(User, db_column="Current_Research_Advisor", on_delete=models.PROTECT, related_name='research_advisor', blank=True, null=True)

    class Meta:
        unique_together = ('username', 'Questionnaire_For',)

    def __str__(self):
        return str(self.username) + " " + str(self.Questionnaire_For) + " " + self.Topic
