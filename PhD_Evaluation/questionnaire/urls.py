from django.urls import path
from django.conf.urls import url
from questionnaire import views

app_name = 'questionnaire'

urlpatterns = [
    # path('submissions/(?P<item_id>[0-9]+)', views.viewSubmissions, name='submissions'),
    path('submissions/', views.viewSubmissions, name='submissions'),
]
