from django.shortcuts import render,redirect
from . import forms,models
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from therapist import models as TMODEL
from patient import models as PMODEL
from therapist import forms as TFORM
from patient import forms as PFORM
from django.contrib.auth.models import User



def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'quiz/index.html')


def is_therapist(user):
    return user.groups.filter(name='THERAPIST').exists()

def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def afterlogin_view(request):
    if is_patient(request.user):      
        return redirect('patient/patient-dashboard')
                
    elif is_therapist(request.user):
        accountapproval=TMODEL.Therapist.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('therapist/therapist-dashboard')
        else:
            return render(request,'therapist/therapist_wait_for_approval.html')
    else:
        return redirect('admin-dashboard')



def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict={
    'total_patient':PMODEL.Patient.objects.all().count(),
    'total_therapist':TMODEL.Therapist.objects.all().filter(status=True).count(),
    'total_course':models.Course.objects.all().count(),
    'total_question':models.Question.objects.all().count(),
    }
    return render(request,'quiz/admin_dashboard.html',context=dict)

@login_required(login_url='adminlogin')
def admin_therapist_view(request):
    dict={
    'total_therapist':TMODEL.Therapist.objects.all().filter(status=True).count(),
    'pending_therapist':TMODEL.Therapist.objects.all().filter(status=False).count(),
    'salary':TMODEL.Therapist.objects.all().filter(status=True).aggregate(Sum('salary'))['salary__sum'],
    }
    return render(request,'quiz/admin_therapist.html',context=dict)

@login_required(login_url='adminlogin')
def admin_view_therapist_view(request):
    therapists= TMODEL.Therapist.objects.all().filter(status=True)
    return render(request,'quiz/admin_view_therapist.html',{'therapists':therapists})


@login_required(login_url='adminlogin')
def update_therapist_view(request,pk):
    therapist=TMODEL.Therapist.objects.get(id=pk)
    user=TMODEL.User.objects.get(id=therapist.user_id)
    userForm=TFORM.TherapistUserForm(instance=user)
    therapistForm=TFORM.TherapistForm(request.FILES,instance=therapist)
    mydict={'userForm':userForm,'therapistForm':therapistForm}
    if request.method=='POST':
        userForm=TFORM.TherapistUserForm(request.POST,instance=user)
        therapistForm=TFORM.TherapistForm(request.POST,request.FILES,instance=therapist)
        if userForm.is_valid() and therapistForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            therapistForm.save()
            return redirect('admin-view-therapist')
    return render(request,'quiz/update_therapist.html',context=mydict)



@login_required(login_url='adminlogin')
def delete_therapist_view(request,pk):
    therapist=TMODEL.Therapist.objects.get(id=pk)
    user=User.objects.get(id=therapist.user_id)
    user.delete()
    therapist.delete()
    return HttpResponseRedirect('/admin-view-therapist')




@login_required(login_url='adminlogin')
def admin_view_pending_therapist_view(request):
    therapists= TMODEL.Therapist.objects.all().filter(status=False)
    return render(request,'quiz/admin_view_pending_therapist.html',{'therapists':therapists})


@login_required(login_url='adminlogin')
def approve_therapist_view(request,pk):
    therapistSalary=forms.TherapistSalaryForm()
    if request.method=='POST':
        therapistSalary=forms.TherapistSalaryForm(request.POST)
        if therapistSalary.is_valid():
            therapist=TMODEL.Therapist.objects.get(id=pk)
            therapist.salary=therapistSalary.cleaned_data['salary']
            therapist.status=True
            therapist.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-pending-therapist')
    return render(request,'quiz/salary_form.html',{'therapistSalary':therapistSalary})

@login_required(login_url='adminlogin')
def reject_therapist_view(request,pk):
    therapist=TMODEL.Therapist.objects.get(id=pk)
    user=User.objects.get(id=therapist.user_id)
    user.delete()
    therapist.delete()
    return HttpResponseRedirect('/admin-view-pending-therapist')

@login_required(login_url='adminlogin')
def admin_view_therapist_salary_view(request):
    therapists= TMODEL.Therapist.objects.all().filter(status=True)
    return render(request,'quiz/admin_view_therapist_salary.html',{'therapists':therapists})




@login_required(login_url='adminlogin')
def admin_patient_view(request):
    dict={
    'total_patient':PMODEL.Patient.objects.all().count(),
    }
    return render(request,'quiz/admin_patient.html',context=dict)

@login_required(login_url='adminlogin')
def admin_view_patient_view(request):
    patients= PMODEL.Patient.objects.all()
    return render(request,'quiz/admin_view_patient.html',{'patients':patients})



@login_required(login_url='adminlogin')
def update_patient_view(request,pk):
    patient=PMODEL.Patient.objects.get(id=pk)
    user=PMODEL.User.objects.get(id=patient.user_id)
    userForm=PFORM.PatientUserForm(instance=user)
    patientForm=PFORM.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=PFORM.PatientUserForm(request.POST,instance=user)
        patientForm=PFORM.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patientForm.save()
            return redirect('admin-view-patient')
    return render(request,'quiz/update_patient.html',context=mydict)



@login_required(login_url='adminlogin')
def delete_patient_view(request,pk):
    patient=PMODEL.Patient.objects.get(id=pk)
    user=User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return HttpResponseRedirect('/admin-view-patient')


@login_required(login_url='adminlogin')
def admin_course_view(request):
    return render(request,'quiz/admin_course.html')


@login_required(login_url='adminlogin')
def admin_add_course_view(request):
    courseForm=forms.CourseForm()
    if request.method=='POST':
        courseForm=forms.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-course')
    return render(request,'quiz/admin_add_course.html',{'courseForm':courseForm})


@login_required(login_url='adminlogin')
def admin_view_course_view(request):
    courses = models.Course.objects.all()
    return render(request,'quiz/admin_view_course.html',{'courses':courses})

@login_required(login_url='adminlogin')
def delete_course_view(request,pk):
    course=models.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/admin-view-course')



@login_required(login_url='adminlogin')
def admin_question_view(request):
    return render(request,'quiz/admin_question.html')


@login_required(login_url='adminlogin')
def admin_add_question_view(request):
    questionForm=forms.QuestionForm()
    if request.method=='POST':
        questionForm=forms.QuestionForm(request.POST,request.FILES)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=models.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-question')
    return render(request,'quiz/admin_add_question.html',{'questionForm':questionForm})


@login_required(login_url='adminlogin')
def admin_view_question_view(request):
    courses= models.Course.objects.all()
    return render(request,'quiz/admin_view_question.html',{'courses':courses})

@login_required(login_url='adminlogin')
def view_question_view(request,pk):
    questions=models.Question.objects.all().filter(course_id=pk)
    return render(request,'quiz/view_question.html',{'questions':questions})

@login_required(login_url='adminlogin')
def delete_question_view(request,pk):
    question=models.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/admin-view-question')

@login_required(login_url='adminlogin')
def admin_view_patient_marks_view(request):
    patients= PMODEL.Patient.objects.all()
    return render(request,'quiz/admin_view_patient_marks.html',{'patients':patients})

@login_required(login_url='adminlogin')
def admin_view_marks_view(request,pk):
    courses = models.Course.objects.all()
    response =  render(request,'quiz/admin_view_marks.html',{'courses':courses})
    response.set_cookie('patient_id',str(pk))
    return response

@login_required(login_url='adminlogin')
def admin_check_marks_view(request,pk):
    course = models.Course.objects.get(id=pk)
    patient_id = request.COOKIES.get('patient_id')
    patient= PMODEL.Patient.objects.get(id=patient_id)

    results= models.Result.objects.all().filter(course=course).filter(patient=patient)
    return render(request,'quiz/admin_check_marks.html',{'results':results})

def aboutus_view(request):
    return render(request,'quiz/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'quiz/contactussuccess.html')
    return render(request, 'quiz/contactus.html', {'form':sub})


