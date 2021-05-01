from django.shortcuts import render,redirect
from .forms import Registration

# Create your views here.
def register(request):
	if request.method == "POST":
		form = Registration(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/login")
	else:
		form = Registration()
	return render(request,"task/bye.html",{"form":form})

def quiz(request):
	return render(request,"task/index.html")

def answers(request):
	responses = []
	answers = ['python','19','semicolon','3.9','no']
	if request.method == 'POST':
		q1 = request.POST['q1']
		q2 = request.POST['q2']
		q3 = request.POST['q3']
		q4 = request.POST['q4']
		q5 = request.POST['q5']
		responses.append(q1)
		responses.append(q2)
		responses.append(q3)
		responses.append(q4)
		responses.append(q5)
		if responses == answers:
			return render(request,'task/correct.html', {"answers" : answers , "responses" : responses})
		else:
			return render(request,'task/wrong.html', {"answers" : answers , "responses" : responses})
