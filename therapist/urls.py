from django.urls import path
from therapist import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('therapistclick', views.therapistclick_view),
path('therapistlogin', LoginView.as_view(template_name='therapist/therapistlogin.html'),name='therapistlogin'),
path('therapistsignup', views.therapist_signup_view,name='therapistsignup'),
path('therapist-dashboard', views.therapist_dashboard_view,name='therapist-dashboard'),
path('therapist-exam', views.therapist_exam_view,name='therapist-exam'),
path('therapist-add-exam', views.therapist_add_exam_view,name='therapist-add-exam'),
path('therapist-view-exam', views.therapist_view_exam_view,name='therapist-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),


path('therapist-question', views.therapist_question_view,name='therapist-question'),
path('therapist-add-question', views.therapist_add_question_view,name='therapist-add-question'),
path('therapist-view-question', views.therapist_view_question_view,name='therapist-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]