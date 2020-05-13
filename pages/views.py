from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp = next((x for x in realtors if x.is_mvp == True), realtors[0])
   
    context = {
        'realtors':realtors,
        'mvp': mvp,
    }
    return render(request, 'pages/about.html', context)