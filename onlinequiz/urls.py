from django.urls import path,include
from django.contrib import admin
from quiz import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('therapist/',include('therapist.urls')),
    path('patient/',include('patient.urls')),
    


    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='quiz/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),



    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='quiz/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-therapist', views.admin_therapist_view,name='admin-therapist'),
    path('admin-view-therapist', views.admin_view_therapist_view,name='admin-view-therapist'),
    path('update-therapist/<int:pk>', views.update_therapist_view,name='update-therapist'),
    path('delete-therapist/<int:pk>', views.delete_therapist_view,name='delete-therapist'),
    path('admin-view-pending-therapist', views.admin_view_pending_therapist_view,name='admin-view-pending-therapist'),
    path('admin-view-therapist-salary', views.admin_view_therapist_salary_view,name='admin-view-therapist-salary'),
    path('approve-therapist/<int:pk>', views.approve_therapist_view,name='approve-therapist'),
    path('reject-therapist/<int:pk>', views.reject_therapist_view,name='reject-therapist'),

    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('admin-view-patient-marks', views.admin_view_patient_marks_view,name='admin-view-patient-marks'),
    path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
    path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('delete-patient/<int:pk>', views.delete_patient_view,name='delete-patient'),

    path('admin-course', views.admin_course_view,name='admin-course'),
    path('admin-add-course', views.admin_add_course_view,name='admin-add-course'),
    path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
    path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>', views.view_question_view,name='view-question'),
    path('delete-question/<int:pk>', views.delete_question_view,name='delete-question'),


]
