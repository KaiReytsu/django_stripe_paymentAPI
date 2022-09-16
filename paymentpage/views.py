import stripe
from django.conf import settings
from django.http import Http404, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from rest_framework.views import APIView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

class ItemDetailView(DetailView):
    '''Item detail page'''
    model = Item
    template_name = 'itemdetail.html'

class PaymentView(APIView):
    permission_classes = ()
    authentication_classes = ()
    def get_object(self, pk):
        '''Check if item with the 
        given id is in the database'''
        try:
            return Item.objects.get(id=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''Function for processing the get 
        method to get the session id'''
        item = self.get_object(pk)
        session = stripe.checkout.Session.create(
            line_items = [{
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': item.price,
                    'product_data': {
                        'name': item.name
                        }
                    },
                'quantity': 1
            }],
            mode = 'payment',
            success_url = request.build_absolute_uri('/success/'),
            cancel_url = request.build_absolute_uri('/cancel/')
        )
        return JsonResponse({'sessionid': session.id})

class SuccessView(TemplateView):
    '''View to display the success payment'''
    template_name = "success.html"

class CancelView(TemplateView):
    '''View to display the cancel payment page'''
    template_name = "cancel.html"

    

