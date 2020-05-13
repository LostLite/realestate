from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'listings':page_obj
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {
        'listing':listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')