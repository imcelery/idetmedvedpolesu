from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            content = {}
            content = form.cleaned_data
            return render(request, "blog/otvet.html", content)

    else:
        form = NameForm()

    return render(request, "blog/name.html", {"form": form})

