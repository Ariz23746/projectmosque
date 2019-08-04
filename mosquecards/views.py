from django.shortcuts import render, get_object_or_404, redirect
from .models import mosquecards
from django.contrib.auth.decorators import login_required
from django.template import Library





def search(request):

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(MosqueName__icontains=query)
		return render(request, 'mosquecards/mosquedetails.html', {'details':mosquedetails})


def home(request):

    cards = mosquecards.objects
    return render(request, 'mosquecards/home.html',{'cards':cards})


def mosquedetails(request, mosque_id):

	mosquedetails = get_object_or_404(mosquecards, pk=mosque_id)
	return render(request, 'mosquecards/mosquedetails.html', {'details':mosquedetails})

def addmosquedetails(request):

	details = mosquecards.objects
	return render(request, 'mosquecards/addmosquedetails.html')

@login_required(login_url="/accounts/signin")
def addmosque(request):
	if request.method == 'POST':
		if request.POST['image'] and request.POST['mosquename'] and request.POST['address'] and request.POST['mosqueBanner'] and request.POST['fajr'] and request.POST['zuhar'] and request.POST['asar'] and request.POST['maghrib'] and request.POST['isha'] :
			mosque = mosquecards()
			mosque.image = request.POST['image']
			mosque.MosqueName = request.POST['mosquename']
			mosque.address = request.POST['address']
			mosque.mosqueBanner = request.POST['mosqueBanner']
			mosque.fajr = request.POST['fajr']
			mosque.zuhar = request.POST['zuhar']
			mosque.asar = request.POST['asar']
			mosque.maghrib = request.POST['maghrib']
			mosque.isha = request.POST['isha']
			mosque.save()
			return redirect('home')


		else:
			return render(request, 'mosquecards/addmosque.html',{'error':'All fields are required'})
	else:	
		return render(request, 'mosquecards/addmosque.html')

def aboutus(request):
	return render(request, 'mosquecards/aboutus.html')

'''def search(request):
	return render(request, 'mosquecards/search.html')'''			






# Create your views here.
