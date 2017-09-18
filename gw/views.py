from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import GwModelForm
from .utils import gw_model
import numpy as np
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GwModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            n = form.cleaned_data['n']
            hini = form.cleaned_data['hini']
            rf = form.cleaned_data['rf']
            sy = form.cleaned_data['sy']
            hmin = form.cleaned_data['hmin']
            pd = form.cleaned_data['pd']
            rain = np.random.rand(n)
            draft = 0.1 * np.random.rand(n, )
            h, baseflow = gw_model(hini, rf, sy, hmin, pd, rain, draft)

            # redirect to a new URL:
            return JsonResponse({
                'h': h.tolist(),
                'baseflow': baseflow.tolist()
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GwModelForm()

    return render(request, "gw/index.html", {'form': form})
