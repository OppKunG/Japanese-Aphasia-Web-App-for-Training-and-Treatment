from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from quiz import models as QMODEL
from patient import models as SMODEL
from quiz import forms as QFORM


#for showing signup/login button for therapist
def therapistclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'therapist/therapistclick.html')

def therapist_signup_view(request):
    userForm=forms.TherapistUserForm()
    therapistForm=forms.TherapistForm()
    mydict={'userForm':userForm,'therapistForm':therapistForm}
    if request.method=='POST':
        userForm=forms.TherapistUserForm(request.POST)
        therapistForm=forms.TherapistForm(request.POST,request.FILES)
        if userForm.is_valid() and therapistForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            therapist=therapistForm.save(commit=False)
            therapist.user=user
            therapist.save()
            my_therapist_group = Group.objects.get_or_create(name='THERAPIST')
            my_therapist_group[0].user_set.add(user)
        return HttpResponseRedirect('therapistlogin')
    return render(request,'therapist/therapistsignup.html',context=mydict)



def is_therapist(user):
    return user.groups.filter(name='THERAPIST').exists()

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def therapist_dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    'total_patient':SMODEL.Patient.objects.all().count()
    }
    return render(request,'therapist/therapist_dashboard.html',context=dict)

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def therapist_exam_view(request):
    return render(request,'therapist/therapist_exam.html')


@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def therapist_add_exam_view(request):
    courseForm=QFORM.CourseForm()
    if request.method=='POST':
        courseForm=QFORM.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/therapist/therapist-view-exam')
    return render(request,'therapist/therapist_add_exam.html',{'courseForm':courseForm})

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def therapist_view_exam_view(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'therapist/therapist_view_exam.html',{'courses':courses})

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def delete_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/therapist/therapist-view-exam')

@login_required(login_url='adminlogin')
def therapist_question_view(request):
    return render(request,'therapist/therapist_question.html')

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def therapist_add_question_view(request):
    questionForm=QFORM.QuestionForm()
    if request.method=='POST':
        questionForm=QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return HttpResponseRedirect('/therapist/therapist-view-question')
    return render(request,'therapist/therapist_add_question.html',{'questionForm':questionForm})

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def therapist_view_question_view(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'therapist/therapist_view_question.html',{'courses':courses})

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def see_question_view(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'therapist/see_question.html',{'questions':questions})

@login_required(login_url='therapistlogin')
@user_passes_test(is_therapist)
def remove_question_view(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/therapist/therapist-view-question')
