from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Listing

# Create your views here.
def list_home(request):
    listings=Listing.objects.all()
    paginator=Paginator(listings,2)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context={
        'listing' : listing 
    }
    return render(request,'listings/listing.html',context)

def search(request):
    listings=Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keyword=request.GET['keywords']
        if keyword:
            listings=listings.filter(description__icontains = keyword)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            listings=listings.filter(city__iexact = city)
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            listings=listings.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms=int(request.GET['bedrooms'])
        if bedrooms:
            listings=listings.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            listings=listings.filter(price__lte = price)
    context={
        'listings':listings
    }
    return render(request,'listings/search.html',context)