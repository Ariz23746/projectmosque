from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse


from django.contrib import auth



def signup(request):
	if request.method == 'POST':

		if request.POST['password'] == request.POST['confirmpassword']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'mosqueaccount/signup.html', {'error':'Username has already been taken'})
			except User.DoesNotExist:
				User.objects.create_user(request.POST['username'], password=request.POST['password'])
				auth.login(request,user)
				return redirect('home')

		else:
			return render(request, 'mosqueaccount/signup.html',{'error':'password must match'})
	else:
		
		return render(request, 'mosqueaccount/signup.html')

def signin(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request ,'mosqueaccount/signin.html',{'error':'your username or password is wrong'})
	else:
		return render(request,'mosqueaccount/signin.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')


	 