from django.contrib import admin
from .models import submissionTrack, course, qualifyingExam, examAttempt
from .models import techingAssistant, paper, research, questionnaire

# admin.site.register(semester)
# admin.site.register(advisor)
# admin.site.register(year)
admin.site.register(submissionTrack)
admin.site.register(course)
admin.site.register(qualifyingExam)
admin.site.register(examAttempt)
admin.site.register(techingAssistant)
admin.site.register(paper)
admin.site.register(research)
admin.site.register(questionnaire)