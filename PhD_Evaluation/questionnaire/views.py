from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import (
	submissionTrack as Submission, 
	course as Course, 
	paper as Paper,
	techingAssistant as TA,
	research as Research,
	examAttempt as QExam,
	questionnaire as Questionnaire
)
from .forms import (
	CourseForm,
	QExamForm,
	TeachingForm,
	ResearchForm,
	PaperForm
)


def home(request):
    context = {
        'reports': Questionnaire.objects.filter(isOpen="Closed")
    }
    return render(request, 'questionnaire/home.html', context)

def questionnaire(request):

	if request.method == 'POST':
		course_form = CourseForm(request.POST)
		if course_form.is_valid():
			course_form.username = request.user.username
			course_form.save()
			return redirect('questionnaire-form')
	else:
	    course_form = CourseForm()

	context = {
		'course_form':course_form
	}
	return render(request, 'questionnaire/questionnaire.html', context)

def saveCourses(request):
	user = request.user
	CourseFormSet = formset_factory(CourseForm)
	courses = Course.objects.filter(username=user, Questionnaire_For='2019').order_by('Questionnaire_For')
	course_data=[{
    'username':c.username, 'Questionnaire_For':c.Questionnaire_For,
    'Subject_Name':c.Subject_Name, 'Subject_Code':c.Subject_Code,
    'Subject_Term_and_Year':c.Subject_Term_and_Year, 'Grade':c.Grade
    } for c in courses]

	if request.method == 'POST':
		course_formset = CourseFormSet(request.POST)
		if course_formset.is_valid():
			new_courses=[]
			for course_form in course_formset:
				username	= course_form.cleaned_data.get('username')
				Questionnaire_For	= course_form.cleaned_data.get('Questionnaire_For')
				Subject_Name	= course_form.cleaned_data.get('Subject_Name')
				Subject_Code	= course_form.cleaned_data.get('Subject_Code')
				Subject_Term_and_Year	= course_form.cleaned_data.get('Subject_Term_and_Year')
				Grade	= course_form.cleaned_data.get('Grade')

				new_courses.append(Course(
					username=username, Questionnaire_For=Questionnaire_For, Subject_Name=Subject_Name, 
					Subject_Code=Subject_Code, Subject_Term_and_Year=Subject_Term_and_Year, Grade=Grade
				))
			try:
				with transaction.atomic():
					#Replace the old with the new
					Course.objects.filter(username=user,Questionnaire_For='2019').delete()
					Course.objects.bulk_create(new_courses)

					# notify our users that Courses are saved
					messages.success(request, 'Your courses are saved.')
					return redirect('questionnaire-form-courses')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your courses.')
				return redirect(reverse('questionnaire-home'))
	else:
		course_formset=CourseFormSet(initial=course_data)

	context = {
		'course_formset' : course_formset
	}
	return render(request, 'questionnaire/step1.html', context)
    		
def saveQExams(request):
	user = request.user
	QExamFormSet = formset_factory(QExamForm)
	qexams = QExam.objects.filter(username=user, Questionnaire_For='2019').order_by('Questionnaire_For')
	qexam_data=[{
    'username':c.username, 'Questionnaire_For':c.Questionnaire_For,
    'Subject_Name':c.Exam_Name, 'Attempt_Number':c.Attempt_Number, 'Grade':c.Grade
    } for c in qexams]

	if request.method == 'POST':
		qexam_formset = QExamFormSet(request.POST)
		if qexam_formset.is_valid():
			new_qexams=[]
			for qexam_form in qexam_formset:
				username	= qexam_form.cleaned_data.get('username')
				Questionnaire_For	= qexam_form.cleaned_data.get('Questionnaire_For')
				Exam_Name	= qexam_form.cleaned_data.get('Exam_Name')
				Attempt_Number	= qexam_form.cleaned_data.get('Attempt_Number')
				Grade	= qexam_form.cleaned_data.get('Grade')

				new_qexams.append(QExam(
					username=username, Questionnaire_For=Questionnaire_For, Exam_Name=Exam_Name, 
					Attempt_Number=Attempt_Number, Grade=Grade
				))
			try:
				with transaction.atomic():
					#Replace the old with the new
					QExam.objects.filter(username=user,Questionnaire_For='2019').delete()
					QExam.objects.bulk_create(new_qexams)

					# notify our users that QExams are saved
					messages.success(request, 'Your qualification exams are saved.')
					return redirect('questionnaire-form-qexams')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your qualification exams.')
				return redirect(reverse('questionnaire-home'))
	else:
		qexam_formset=QExamFormSet(initial=qexam_data)

	context = {
		'qexam_formset' : qexam_formset
	}
	return render(request, 'questionnaire/step2.html', context)

def saveTA(request):
	user = request.user
	TAFormSet = formset_factory(TeachingForm)
	teaching_assists = TA.objects.filter(username=user, Questionnaire_For='2019').order_by('Questionnaire_For')
	ta_data=[{
    'username':c.username, 'Questionnaire_For':c.Questionnaire_For,
    'Subject_Name':c.Exam_Name, 'Subject_Code':c.Subject_Code, 'Responsibilities':c.Responsibilities,
    'In_Which_Semester':c.In_Which_Semester, 'Instructor_Name':c.Instructor_Name, 
    'Lecture_or_Presentation_Given':c.Lecture_or_Presentation_Given, 
    'Area_of_Improvement':c.Area_of_Improvement
    } for c in teaching_assists]

	if request.method == 'POST':
		ta_formset = TAFormSet(request.POST)
		if ta_formset.is_valid():
			new_teaching_assists=[]
			for ta_form in ta_formset:
				username	= ta_form.cleaned_data.get('username')
				Questionnaire_For	= ta_form.cleaned_data.get('Questionnaire_For')
				Subject_Name	= ta_form.cleaned_data.get('Subject_Name')
				Subject_Code	= ta_form.cleaned_data.get('Subject_Code')
				In_Which_Semester = ta_form.cleaned_data.get('In_Which_Semester')
				Instructor_Name	= ta_form.cleaned_data.get('Instructor_Name')
				Responsibilities	= ta_form.cleaned_data.get('Responsibilities')
				Lecture_or_Presentation_Given	= ta_form.cleaned_data.get('Lecture_or_Presentation_Given')
				Area_of_Improvement	= ta_form.cleaned_data.get('Area_of_Improvement')

				new_teaching_assists.append(TA(
					username=username, Questionnaire_For=Questionnaire_For, Subject_Name=Exam_Name, 
					Subject_Code=Subject_Code, Responsibilities=Responsibilities,
					In_Which_Semester=In_Which_Semester, Instructor_Name=Instructor_Name, 
					Lecture_or_Presentation_Given=Lecture_or_Presentation_Given,
					Area_of_Improvement=Area_of_Improvement
				))
			try:
				with transaction.atomic():
					#Replace the old with the new
					TA.objects.filter(username=user,Questionnaire_For='2019').delete()
					TA.objects.bulk_create(new_teaching_assists)

					# notify our users that TAs are saved
					messages.success(request, 'Your teaching assist experiences are saved.')
					return redirect('questionnaire-form-teaching')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your teaching assist experiences .')
				return redirect(reverse('questionnaire-home'))
	else:
		ta_formset=TAFormSet(initial=ta_data)

	context = {
		'ta_formset' : ta_formset
	}
	return render(request, 'questionnaire/step3.html', context)

def saveResearch(request):
	user = request.user
	
	research = Research.objects.filter(username=user, Questionnaire_For='2019').order_by('Questionnaire_For')
	print(str(research))
	research_data=[{
    'username':c.username, 'Questionnaire_For':c.Questionnaire_For,
    'Topic':c.Topic, 'Proposal':c.Proposal, 'Defense':c.Defense, 
    'Current_Academic_Advisor':c.Current_Academic_Advisor, 'Current_Research_Advisor':c.Current_Research_Advisor
    } for c in research]

	if request.method == 'POST':
		research_form = ResearchForm(request.POST)
		if research_form.is_valid():
			username = research_form.cleaned_data.get('username')
			Questionnaire_For = research_form.cleaned_data.get('Questionnaire_For')
			Topic = research_form.cleaned_data.get('Topic')
			Proposal = research_form.cleaned_data.get('Proposal')
			Defense	= research_form.cleaned_data.get('Defense')
			Current_Academic_Advisor = research_form.cleaned_data.get('Current_Academic_Advisor')
			Current_Research_Advisor = research_form.cleaned_data.get('Current_Research_Advisor')
			try:
				with transaction.atomic():
					#Replace the old with the new
					Research.objects.filter(username=user,Questionnaire_For='2019').delete()
					Research.objects.create(new_qexams)

					# notify our users that research details are saved
					messages.success(request, 'Your research details are saved.')
					return redirect('questionnaire-form-research')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your research details.')
				return redirect(reverse('questionnaire-home'))
	else:
		research_form=ResearchForm(initial=research_data)

	context = {
		'research_form' : research_form
	}
	return render(request, 'questionnaire/step4.html', context)

def savePapers(request):
	user = request.user
	PaperFormSet = formset_factory(PaperForm)
	papers = Paper.objects.filter(Author=user, Questionnaire_For='2019').order_by('Questionnaire_For')
	paper_data=[{
	'Author':c.Author, 'Questionnaire_For':c.Questionnaire_For, 'Title':c.Title, 
	'Venue':c.Venue, 'Coauthor':c.Coauthor
    } for c in papers]

	if request.method == 'POST':
		paper_formset = PaperFormSet(request.POST)
		if paper_formset.is_valid():
			new_papers=[]
			for paper_form in paper_formset:
				Author	= paper_form.cleaned_data.get('Author')
				Questionnaire_For	= paper_form.cleaned_data.get('Questionnaire_For')
				Title	= paper_form.cleaned_data.get('Title')
				Venue	= paper_form.cleaned_data.get('Venue')
				Coauthor	= paper_form.cleaned_data.get('Coauthor')

				new_papers.append(Paper(
					Author=Author, Questionnaire_For=Questionnaire_For, Title=Title, 
					Venue=Venue, Coauthor=Coauthor
				))
			try:
				with transaction.atomic():
					#Replace the old with the new
					Paper.objects.filter(Author=user,Questionnaire_For='2019').delete()
					Paper.objects.bulk_create(new_papers)

					# notify our users that papers are saved
					messages.success(request, 'Your papers are saved.')
					return redirect('questionnaire-form-papers')

			except IntegrityError: #If the transaction failed
				messages.error(request, 'There was an error saving your papers.')
				return redirect(reverse('questionnaire-home'))
	else:
		paper_formset=PaperFormSet(initial=paper_data)

	context = {
		'paper_formset' : paper_formset
	}
	return render(request, 'questionnaire/step5.html', context)


class PaperListView(LoginRequiredMixin, ListView):
	model = Paper
	# <app>/<model>_<viewtype>.html
	context_object_name = 'papers'
	ordering = ['title']

class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    # <app>/<model>_<viewtype>.html
    context_object_name = 'courses'
    ordering = ['username', 'Questionnaire_For', 'Subject_Code']


class PaperDetailView(LoginRequiredMixin, DetailView):
    model = Paper


class PaperCreateView(LoginRequiredMixin, CreateView):
    model = Paper
    fields = ['title', 'venue', 'status', 'author', 'coauthors']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PaperUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Paper
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        paper = self.get_object()
        if self.request.user == paper.author:
            return True
        return False


class PaperDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Paper
    success_url = '/'

    def test_func(self):
        paper = self.get_object()
        if self.request.user == paper.author:
            return True
        return False


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['Subject_Name', 'Subject_Code', 'Subject_Term_and_Year', 'Grade']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Course
    success_url = '/'
    fields = ['Subject_Name', 'Subject_Code', 'Subject_Term_and_Year', 'Grade']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.username:
            return True
        return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/'

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.username:
            return True
        return False
