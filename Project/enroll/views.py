from ast import Sub
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'Home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        if Student.objects.filter(stu_user=username).exists():
            return HttpResponse('Username already exists.')
        else:
            user = Student.objects.create(stu_user=username, stu_pass=password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        check_user = Student.objects.filter(stu_user=username, stu_pass=password)
        user = auth.authenticate(username= username , password = password)
        if check_user:
            request.session['user'] = request.POST['username']
            return redirect('webhome')
        elif user is not None:
            allstd = Student.objects.all()
            content = {'allstd':allstd}
            return render(request,'classresult.html',content)
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request,'login.html')



def examonline(request, exam_name ):
    if not request.session.has_key('user'):
        return redirect('login')
    else:
        a = Subject.objects.get(subname = exam_name) 
        print("a:- ",a.id)
        result = Question.objects.filter(subject = a)
        for i in result:
            print(i)
        return render(request,'index1.html',{'Exam':result , 'exam_name': exam_name})

def showresult(request, exam_name):
    if not request.session.has_key('user'):
        return redirect('login')
    else:
        marks = 0
        sub = Subject.objects.get(subname = exam_name) 
        # a = Question.objects.filter(subject = sub) 
        # print("a:- ",a)
        # result = Question.objects.all()
        result = Question.objects.filter(subject = sub)
        print("result is:-  ",result)
        if request.method == 'POST':
            for i in result:
                try:
                    answer = request.POST[str(i.id)]
                    print("Answer")
                    print("option : - ",answer)
                    if answer == i.Corrans:
                        marks +=1
                    else:
                        marks +=0
                except Exception as e:
                    print(e)
            res = Student.objects.get(stu_user = request.session['user'])
            if exam_name == 'Python':
                res.stu_marks = marks
                res.save()
            elif exam_name == 'Java':
                res.stu_marks_java = marks
                res.save()
            else : 
                res.stu_marks_php = marks
                res.save()
            if marks<3:
                a = "fail"  
            else:
                a = "Pass"
            context = {'res':marks,'a':a}
            return render(request,'result.html',context)
        return render(request,'index1.html')


def webhome(request):
    if not request.session.has_key('user'):
        return redirect('login')
    else:
        return render(request,'web.html')


def subname(request):
    alldata = Student.objects.all()
    for i in alldata:
        print(i)

def test(request):
    
    return redirect(request,'homeindex.html')

def logout(request):
    request.session.pop('user',None)
    return redirect('login')