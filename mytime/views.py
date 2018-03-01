import random
from django.shortcuts import render_to_response
#from django.shortcuts import render

# Create your views here.


def rnd(request):
    return render_to_response('rnd.html', {'rnd': str(random.random())})
