
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    #path('mosques', mosquecard.views.home, name='home'),
    #path('mosques', mosquecard.views.mosquedetails, name='mosquedetails'),
     path('home/', include('mosquecards.urls')),
     path('accounts/', include('mosqueaccount.urls')),
     




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

