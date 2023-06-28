from django.urls import path
from therapist import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('therapistclick', views.therapistclick_view),
path('therapistlogin', LoginView.as_view(template_name='therapist/therapistlogin.html'),name='therapistlogin'),
path('therapistsignup', views.therapist_signup_view,name='therapistsignup'),
path('therapist-dashboard', views.therapist_dashboard_view,name='therapist-dashboard'),
path('therapist-course', views.therapist_course_view,name='therapist-course'),
path('therapist-add-course', views.therapist_add_course_view,name='therapist-add-course'),
path('therapist-view-course', views.therapist_view_course_view,name='therapist-view-course'),
path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),


path('therapist-question', views.therapist_question_view,name='therapist-question'),
path('therapist-add-question', views.therapist_add_question_view,name='therapist-add-question'),
path('therapist-view-question', views.therapist_view_question_view,name='therapist-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]