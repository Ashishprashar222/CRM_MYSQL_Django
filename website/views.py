from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddDetailForm
from .models import Records
# Create your views here.
def home(request):
	record= Records.objects.all()

	# check to see if user is login
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		# authenticate
		user= authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"You have be logged In..")
			return redirect('home')
		else:
			messages.success(request,"Please Try again with valid credentials...")
			return redirect('home')
	else:
		return render(request,'home.html',{'record':record})

# def login_user(request):
# 	pass

def logout_user(request):
	logout(request)
	messages.success(request,"you have been logged out")
	return redirect('home')

def register_user(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# authenticate and login
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(username=username,password=password)
			login(request,user)
			messages.success(request,"You have successfully registered")
			return redirect('home')
	else:
		form=SignUpForm()
		return render(request,'register.html',{'form':form})
		
	return render(request, 'register.html', {'form':form})


def detail(request,pk):
	if request.user.is_authenticated:
		#Look up rocord
		detail=Records.objects.get(id=pk)
		return render(request,'detail.html',{'detail':detail})
	else:
		messages.success(request,'You have to logged in to view this page')
		return redirect('home')


def delete_detail(request,pk):
	if request.user.is_authenticated:
		delete_detail=Records.objects.get(id=pk)
		delete_detail.delete()
		messages.success(request,"Detail has been deleted.")
		return redirect('home')
	else:
		messages.success(request,'You have to logged in to view this page')
		return redirect('home')

def add_detail(request):
	form=AddDetailForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method=='POST':
			if form.is_valid():
				add_detail=form.save()
				messages.success(request,"Record Added Successfully.")
				return redirect('home')
		return render(request,'add_detail.html',{'form':form})
	else:
		messages.success(request,"Must be logged In.")
		return redirect('home')



def update_detail(request, pk):
	if request.user.is_authenticated:
		current_record = Records.objects.get(id=pk)
		form = AddDetailForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')