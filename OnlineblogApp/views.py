

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from OnlineblogApp.models import *

# Create your views here.
def Hello(request):
	msg="welcome to django"
	return HttpResponse(msg)
def Hi(request):
	msg="<H1>welcome</H1>"
	msg=msg+"<H1>Gaurav</H1>"
	return HttpResponse(msg)
def welcome(request,name):
	msg="Thanks dear"+name
	return HttpResponse(msg)
def calc(request,a,b):
	msg="sum"+str(a+b)
	msg=msg+"<BR>sub"+str(a-b)
	msg=msg+"<BR>mul"+str(a*b)
	msg=msg+"<BR>div"+str(a/b)
	return HttpResponse(msg)
def show(request):
	return redirect("http://www.facebook.com")
def index(request):
	return render(request,"index.html")
def main(request):
	return render(request,'main.html')
def btech(request):
	return render(request,'btech.html')
def mca(request):
	return render(request,'mca.html')
def datainput(request):
	return render(request,'datainput.html')
@csrf_exempt
def datasave(request):
	a=request.POST.get("userid")
	b=request.POST.get("uname")
	c=request.POST.get("ucity")
	d=request.POST.get("uemail")
	e=request.POST.get("uphone")
	obj=Users(userid=a,uname=b,city=c,email=d,phone=e)
	obj.save()
	return HttpResponse("RecordSaved")
def datausers(request):
	obj=Users.objects.all()
	msg="data<BR>"
	for res in obj:
		msg=msg+"<BR>"+res.userid
		msg=msg+"<BR>"+res.uname
		msg=msg+"<BR>"+res.city
		msg=msg+"<BR>"+res.email
		msg=msg+"<BR>"+res.phone
	return HttpResponse(msg)

def datadelete(request):
	return render(request,'datadelete.html')
@csrf_exempt
def datadel(request):
	a=request.POST.get("userid")
	obj=Users.objects.get(userid=a)
	obj.delete()
	return HttpResponse("record delete")

def datainput(request):
	return render(request,'datainput.html')
@csrf_exempt
def datasave1(request):
	f=request.POST.get("subjectid")
	g=request.POST.get("sname")
	h=request.POST.get("stream")	
	obj=Subject(subjectid=f,sname=g,stream=h)
	obj.save()
	return HttpResponse("RecordSaved")

def datasubject(request):
	obj=Subject.objects.all()
	msg="data<BR>"
	for res in obj:
		msg=msg+"<BR>"+res.subjectid
		msg=msg+"<BR>"+res.sname
		msg=msg+"<BR>"+res.stream
	return HttpResponse(msg)
def datadelete(request):
	return render(request,'datadelete.html')
@csrf_exempt
def datadel1(request):
	f=request.POST.get("subjectid")
	obj=Subject.objects.get(subjectid=f)
	obj.delete()
	return HttpResponse("record delete")

def datainput(request):
	return render(request,'datainput.html')
@csrf_exempt
def datasave2(request):
	a=request.POST.get("blogid")
	b=request.POST.get("userid")
	c=request.POST.get("subjectid")
	d=request.POST.get("blogtext")
	e=request.POST.get("blogdescription")
	f=request.POST.get("rating")
	obj=Blog(blogid=a,userid=b,subjectid=c,blogtext=d,blogdescription=e,rating=f)
	obj.save()
	return HttpResponse("RecordSaved")

def datablog(request):
	obj=Blog.objects.all()
	msg="data<BR>"
	for res in obj:
		msg=msg+"<BR>"+res.blogid
		msg=msg+"<BR>"+res.userid
		msg=msg+"<BR>"+res.subjectid
		msg=msg+"<BR>"+res.blogtext
		msg=msg+"<BR>"+res.blogdescription
		msg=msg+"<BR>"+res.rating
	return HttpResponse(msg)

def datadelete(request):
	return render(request,'datadelete.html')
@csrf_exempt
def datadel2(request):
	a=request.POST.get("blogid")
	obj=Blog.objects.get(blogid=a)
	obj.delete()
	return HttpResponse("record delete")

def datainput(request):
	return render(request,'datainput.html')
@csrf_exempt
def datasave3(request):
	a=request.POST.get("blogid")
	b=request.POST.get("userid")
	c=request.POST.get("rating")	
	obj=Ratine(blogid=a,userid=b,rating=c)
	obj.save()
	return HttpResponse("RecordSaved")

def dataratine(request):
	obj=Ratine.objects.all()
	msg="data<BR>"
	for res in obj:
		msg=msg+"<BR>"+res.blogid
		msg=msg+"<BR>"+res.userid
		msg=msg+"<BR>"+res.rating
	return HttpResponse(msg)
def datadelete(request):
	return render(request,'datadelete.html')
@csrf_exempt
def datadel3(request):
	a=request.POST.get("blogid")
	obj=Ratine.objects.get(blogid=a)
	obj.delete()
	return HttpResponse("record delete")

def home(request):
	return render(request , 'base.html')






