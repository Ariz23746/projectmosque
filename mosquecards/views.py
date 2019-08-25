from django.shortcuts import render, get_object_or_404, redirect
from .models import mosquecards
from django.contrib.auth.decorators import login_required
from django.template import Library
from django.db.models import Q


def home(request):

    cards = mosquecards.objects
    return render(request, 'mosquecards/home.html', {'cards': cards})


def mosquedetails(request, mosque_id):

	cards = mosquecards.objects
	mosquedetails = get_object_or_404(mosquecards, pk=mosque_id)
	return render(request, 'mosquecards/mosquedetails.html', {'details':mosquedetails,'cards': cards})

def addmosquedetails(request):

	details = mosquecards.objects
	return render(request, 'mosquecards/addmosquedetails.html')

@login_required(login_url="/accounts/signin")
def addmosque(request):
	if request.method == 'POST':
		if (request.POST['image'] or request.POST['image2'] or request.POST['image3'] or request.POST['image4'] or request.POST['mosqueBanner']) and (request.POST['mosquename'] and request.POST['address'] and request.POST['fajr'] and request.POST['zuhar'] and request.POST['asar'] and request.POST['maghrib'] and request.POST['isha']) : 
			
			mosque = mosquecards()
			mosque.image = request.POST['image']
			mosque.image2 = request.POST['image2']
			mosque.image3 = request.POST['image3']
			mosque.image4 = request.POST['image4']
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

def search(request):
    queryset_list = mosquecards.objects
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            queryset_list = queryset_list.filter(Q(MosqueName__icontains=q) | Q(address__icontains=q))

    dict = {
    'mosquecards_models':queryset_list,
	'error':'No such Mosque Exist'
    }
    return render(request, 'mosquecards/search.html', dict)

# Create your views here.
