import os
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')    
        listing = request.POST.get('listing')    
        name = request.POST.get('name')    
        email = request.POST.get('email')    
        phone = request.POST.get('phone')    
        message = request.POST.get('message')    
        user_id = request.POST.get('user_id')    
        realtor_email = request.POST.get('realtor_email')    

        # check if user has made enquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)


            if has_contacted:
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)

        contact.save()
        print(os.getenv("mail_username"))
        send_mail(
            f'New Property Listing Enquiry - {listing}',
            f'A new enquiry for {listing} has been made. Sign in to the admin panel for more info.',
            f'{os.getenv("mail_username")}',
            [realtor_email,],
            fail_silently= False
        )
        messages.success(request,'Your request has been received. A realtor will be in touch with you soon')

        return redirect('/listings/'+listing_id)