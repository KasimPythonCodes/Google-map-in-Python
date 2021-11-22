from django.shortcuts import render , redirect
from .models import  Rentall
from .forms import RentallForm
import geocoder
import  folium
from django.http import HttpResponse

def my_functions(request):

        if request.method=='POST':
           form = RentallForm(request.POST)
           if form.is_valid():
              form.save()
              return redirect('/')
        else:
           form=RentallForm()     
        address=Rentall.objects.all().last()
        location=geocoder.osm(address)
        lat=location.lat
        lng=location.lng
        country=location.country
        if lat==None or lng==None:
           address.delete()
           return HttpResponse('You Address Input is Invalid')
        #Create Map Objects
        m=folium.Map(location=[19 , -12], zoom_start=2)
        #folium.Marker([5.594  , -0.219] , tooltip="Click for more" , popup='Ghana').add_to(m)
        folium.Marker([lat  , lng] , tooltip="Click for more" , popup=country).add_to(m)
        # Get html Represention of map Object
        m=m._repr_html_()
        context={
            'm':m,
            'form':form
        }
        return render(request , 'enroll/index.html' , context)



