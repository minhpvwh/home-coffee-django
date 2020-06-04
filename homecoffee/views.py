from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from homecoffee.models import ReviewCustomer


# class HomeCoffeeView(TemplateView):
#     template_name = 'homecoffee.html'


def customer_reviews_view(request):
    object_list = ReviewCustomer.objects.all()[:3]
    return render(request, 'homecoffee.html', {
        'customer_reviews': object_list,
        'mam': 'huyen'
    })
