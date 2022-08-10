from multiprocessing import context
from django.shortcuts import render
from .models import IceCream 
from django.http import Http404

# Create your views here.
    #Fetch the ice cream object based on the id received in the parameter.
def get_ice_cream(request, ice_cream_id):
    try:
        ice_cream = IceCream.objects.get(id=ice_cream_id)
    except IceCream.DoesNotExist:
        raise Http404("Ice Cream does not exist")
    context = {
        'name': ice_cream.name,
        "flavors": ice_cream.flavors.values_list('name'),
        "shop": ice_cream.shop,
        "stock": ice_cream.stock,
    }
    print(context)
    return render(request, 'ice_cream_detail.html', context)