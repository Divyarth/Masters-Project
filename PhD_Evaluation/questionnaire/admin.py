from django.contrib import admin
from questionnaire.models import course, questionnaire, submissionTrack, qualifyingExam, techingAssistant, paper, \
    research, examAttempt  # thesis, advisor,

# Register your models here.
# admin.site.register(year)
# admin.site.register(advisor)
admin.site.register(course)
admin.site.register(submissionTrack)
# admin.site.register(semester)
admin.site.register(questionnaire)
admin.site.register(research)
admin.site.register(qualifyingExam)
admin.site.register(examAttempt)
admin.site.register(techingAssistant)
admin.site.register(paper)
# admin.site.register(thesis)

admin.site.site_header = "PhD Evaluation Administrator"
admin.site.site_title = 'PhD Evaluation'
