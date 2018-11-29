from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .forms import MakeDonationForm, DonorForm     #import forms.py  for created for the payment details 
from django.conf import settings
from django.contrib import messages
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def donation_checkout(request):
    
    donation_form = MakeDonationForm()
    donor_form=DonorForm()
    
    context = {'donation_form':donation_form, 'donor_form':donor_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY} 
   
    
    return render(request, "donation/view_donation.html", context)
    
def submit_donation(request):
    
    donation_form = MakeDonationForm(request.POST)
    donor_form = DonorForm(request.POST) #get the information from the form subbited and i populate it using OrderForm (form made of the order model)***
    
    if donor_form.is_valid() and donation_form.is_valid(): #is valid if i get stripe.id
        
        #grab the money and run
        # donation_total = cart_items_and_total['cart_total'] #get total of the cart
        stripe_token=payment_form.cleaned_data['stripe_id'] # cleaned_data gives me the digits of the card 

        try:

            total_in_cent = int(total*100)
            donor = stripe.Charge.create(
                amount=total_in_cent,
                currency="EUR",
                description="Dummy Transaction", 
                card=stripe_token,
            )

        except stripe.error.CardError:
            print("Declined")
            messages.error(request, "Your card was declined!")

        if donator.paid:
            print("Paid")
            messages.error(request, "You have successfully paid")
        
        return redirect("/") 
