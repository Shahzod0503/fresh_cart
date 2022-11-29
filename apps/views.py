# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.forms import CustomForModel


# Create your views here.


class IndexView(TemplateView):
    template_name = 'order/index.html'

class RegisterView(FormView):
    form_class = CustomForModel
    template_name = 'order/auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ResetView(TemplateView):
    template_name = 'order/auth/reset.html'


class OrdersView(TemplateView):
    template_name = 'order/myaccount/orders.html'
