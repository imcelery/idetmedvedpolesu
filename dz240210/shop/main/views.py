from django.shortcuts import render
from django.http import HttpResponse

from .models import Good, Category
from django.views.generic import TemplateView

def MainView(TemplateView):
    template_name = "main/main.html"

    def get_goods(self, request):
        return Good.objects.all

    def get_base_context(self, request, *args, **kwargs):
        list_categories = Category.objects.all()
        context = {
            "list_goods" :kwargs["list_goods"],
            "list_categories" : list_categories,
            "form" : kwargs["kwargs"]
        }
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass

        context = get_base_context(request, *args, **kwargs)
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = get_base_context(request, *args, **kwargs)
        return render(request, self.template_name, context)
def mainView(request):
    categories_list = Category.objects.all
    goods_list = Good.objects.all
    context = {
        "categories": categories_list,
        "goods": goods_list,
    }
    return render(request, "main/index.html", context)

