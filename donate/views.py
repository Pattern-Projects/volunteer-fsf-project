from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import MakePaymentForm, OrderForm
from django.utils import timezone
from django.conf import settings
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

# @login_required
def donate(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)

            if order_form.is_valid() and payment_form.is_valid():
                order = order_form.save(commit=False)
                order.date = timezone.now()
                order.save()

                try:
                    customer = stripe.Charge.create(
                        amount = int(order.amount),
                        currency = 'EUR',
                        description = request.user.email,
                        card = payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError:
                    messages.error(request, 'Your card was declined!')

                if customer.paid:
                    messages.error(request, 'You have successfully paid. Thank you for your donation')
                    return redirect(reverse('donate'))
                else:
                    messages.error(request, 'Unable to take payment')
            else:
                messages.error(request, "We were unable to process your payment at this time")
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()
        return render(request, 'donate.html', {"order_form":order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
    else:
        return redirect(reverse('login'))
