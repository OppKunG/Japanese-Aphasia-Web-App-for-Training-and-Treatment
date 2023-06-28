from django.urls import path
from patient import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("patientclick", views.patientclick_view),
    path(
        "patientlogin",
        LoginView.as_view(template_name="patient/patientlogin.html"),
        name="patientlogin",
    ),
    path("patientsignup", views.patient_signup_view, name="patientsignup"),
    path("patient-dashboard", views.patient_dashboard_view, name="patient-dashboard"),
    path("patient-course", views.patient_course_view, name="patient-course"),
    path("take-exam/<int:pk>", views.take_exam_view, name="take-exam"),
    path("start-exam/<int:pk>", views.start_exam_view, name="start-exam"),
    path("calculate-marks", views.calculate_marks_view, name="calculate-marks"),
    path("view-result", views.view_result_view, name="view-result"),
    path("check-marks/<int:pk>", views.check_marks_view, name="check-marks"),
    path("patient-marks", views.patient_marks_view, name="patient-marks"),
]
