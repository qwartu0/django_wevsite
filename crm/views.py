from django.shortcuts import render
from crm.models import Orders
from crm.forms import OrdersForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegramm
# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrdersForm()
    dict_obj = {"slider_list":slider_list,
                "pc_1": pc_1,
                "pc_2": pc_2,
                "pc_3": pc_3,
                "price_table": price_table,
                'form': form}

    return render(request, './index.html', dict_obj )



def thanks_page(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    element = Orders(order_name=name, order_phone=phone)
    element.save()
    sendTelegramm(tg_name=name,tg_phone=phone)
    return render(request, 'thanks.html', {"name":name, "phone":phone})

