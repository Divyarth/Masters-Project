from registration.forms import userInfoForm, userInfoForm2  # loginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from registration.models import professorWhiteList, userInfo, announcement  # , studentWhiteList,
from questionnaire.models import submissionTrack, questionnaire, research, techingAssistant, qualifyingExam, paper, \
    examAttempt, course
from registration.models import studentProfile
from django.contrib import messages
import socket

socket.getaddrinfo('127.0.0.1', 8080)


# Create your views here.

@login_required()
def viewSubmissions(request):
    if request.method == 'POST':
        sessionFullName = request.session['fullNameSession']
        sessionUserName = request.session['userNameSession']
        sessionid = request.session['idSession']
        submissionList = submissionTrack.objects.filter(username_id=sessionid).order_by("-questionnaire_for")
        blankspace = ""
        profile = studentProfile.objects.get(email=sessionUserName)
        return render(request, 'registration/homeStudent.html',
                      {'sessionFullName': sessionFullName, 'submissionList': submissionList,
                       'profile': profile, 'blankspace': blankspace})

    else:
        questionnaire_id = request.session["questionnaireForIdSession"]
        questionnaireValue = submissionTrack.objects.get(id=questionnaire_id)
        print("row --> ")
        print(questionnaireValue)

        questionnaireStatus = submissionTrack.objects.get(id=questionnaire_id).status
        questionnaire_submit_username = request.session['userNameSession']
        questionnaire_submit_fullname = request.session['fullNameSession']
        print((questionnaireStatus))

        if questionnaireStatus == "Submitted":

            userTableID = User.objects.get(username=questionnaire_submit_username).id
            course_dict = course.objects.filter(username_id=userTableID, questionnaire_for_id=questionnaire_id)
            examAttempt_dict = examAttempt.objects.filter(username_id=userTableID,
                                                          questionnaire_for_id=questionnaire_id)
            techingAssistant_dict = techingAssistant.objects.filter(username_id=userTableID,
                                                                    questionnaire_for_id=questionnaire_id)
            paper_dict = paper.objects.filter(Author_id=userTableID, questionnaire_for_id=questionnaire_id)
            research_dict = research.objects.filter(username_id=userTableID, questionnaire_for_id=questionnaire_id)

            print(course_dict)
            print(examAttempt_dict)
            print(techingAssistant_dict)
            print(paper_dict)
            print(research_dict)

            return render(request, 'questionnaire/submissionView.html',
                          {'questionnaire_submit_fullname': questionnaire_submit_fullname,
                           'course_dict': course_dict, 'examAttempt_dict': examAttempt_dict,
                           'techingAssistant_dict': techingAssistant_dict, 'paper_dict': paper_dict,
                           'research_dict': research_dict})
        elif questionnaireStatus == "Save":
            return HttpResponse("work in progress")
        ##################saved
        else:
            return HttpResponse("work in progress")
        ##################not started
