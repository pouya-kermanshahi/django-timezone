import datetime

import pytz
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils import timezone
from django.views import View

from orders.forms import AddOrderForm
from orders.models import Order


class AddListView(View):

    def _get_order_list_render(self, request, message=None):

        # tz = request.session.get('django_timezone')

        q = Order.objects.all().order_by('-creation_date')

        if tz is not None:
            # tzinfo = pytz.timezone(tz)
            # time = datetime.datetime.now(tz=tzinfo)
            time = timezone.localtime(timezone.now())
            time = time.replace(hour=13, minute=0)
            time = time.astimezone(pytz.UTC)
            q = q.filter(creation_date__gte=time)

        orders = list(q)
        zones = pytz.all_timezones
        return render(request, 'orders/base.html',
                      context={
                          'orders': orders,
                          'form': AddOrderForm(),
                          'message': message,
                          "timezones": zones
                      }
                      )

    def get(self, request):
        _set_timezone(request)
        message = None
        if request.GET.get("order_created"):
            message = {"text": "Order created successfully", "type": "success"}
        elif request.GET.get("order_deleted"):
            message = {"text": "Order deleted successfully", "type": "success"}

        return self._get_order_list_render(request, message)

    def post(self, request):
        form = AddOrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(name=form.cleaned_data.get("name"))
            return redirect(reverse("list_add_order") + "?" + "order_created=true")
        return redirect(reverse("list_add_order"))


def delete_order(request, order_id):
    if request.method == "POST":
        Order.objects.filter(id=order_id).delete()
        return redirect(reverse("list_add_order") + "?" + "order_deleted=true")
    return redirect(reverse("list_add_order"))


def _set_timezone(request):
    if request.method == 'GET':
        request.session['django_timezone'] = request.GET.get('timezone')
