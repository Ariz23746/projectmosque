from django.shortcuts import render, get_object_or_404, redirect
from .models import mosquecard
from django.contrib.auth.decorators import login_required
from django.template import Library





def home(request):

    cards = mosquecard.objects
    return render(request, 'mosquecard/home.html',{'cards':cards})


def mosquedetails(request, mosque_id):

	mosquedetails = get_object_or_404(mosquecard, pk=mosque_id)
	return render(request, 'mosquecard/mosquedetails.html', {'details':mosquedetails})

def addmosquedetails(request):

	details = mosquecard.objects
	return render(request, 'mosquecard/addmosquedetails.html')

@login_required(login_url="/accounts/signin")
def addmosque(request):
	if request.method == 'POST':
		if request.POST['image'] and request.POST['mosquename'] and request.POST['address'] and request.POST['mosquetime']:
			mosque = mosquecard()
			mosque.image = request.POST['image']
			mosque.MosqueName = request.POST['mosquename']
			mosque.address = request.POST['address']
			mosque.mosqueTime = request.POST['mosquetime']
			mosque.save()
			return redirect('home')


		else:
			return render(request, 'mosquecard/addmosque.html',{'error':'All fields are required'})
	else:	
		return render(request, 'mosquecard/addmosque.html')

def aboutus(request):
	return render(request, 'mosquecard/aboutus.html')

def search(request):
	return render(request, 'mosquecard/search.html')			




		