from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import BiddingForm
from artifacts.models import Artifact
from .models import Bids
from decimal import Decimal

""" Take a bid from the user and check if higher than current bid """
def place_bid(request):
    if request.method=="POST":
        bid_form = BiddingForm(request.POST)
    else:
        bid_form = BiddingForm()
    
    return bid_form
    
def check_bid(request, bid_form, artifact):
    successful_bid = False
    if bid_form.is_valid():
        new_bid = Decimal(request.POST['amount_bid'])
        current_bid = Decimal(artifact.bid)
        if new_bid > current_bid:
            
            email_title = 'Artifact Auctions - '+artifact.name
            email_message_bid = 'You are the highest bidder for '+artifact.name+'. You will be notified if a higher bid is entered.'
            email_message_outbid = 'You have been outbid on '+artifact.name+'. The current bid is now £'+str(new_bid)+'.'
            if artifact.current_bidder:
                send_mail(
                    email_title,
                    email_message_outbid,
                    'admin@artifact-auction.com',
                    [artifact.current_bidder.email],
                    fail_silently=False,)  
                
            artifact.bid = new_bid
            artifact.current_bidder = request.user
            artifact.reserved = True
            artifact.save()
            queryset = Bids.objects.filter(artifact=artifact)
            
            try:
                existing_bid = get_object_or_404(queryset, bidder=request.user)
                existing_bid.bid_amount=new_bid
                existing_bid.save()
            except:
                bid = Bids(bid_amount=new_bid, bidder=request.user, artifact=artifact)
                bid.save()
            messages.success(request, 
                             "You have successfully placed your bid on %s" %artifact.name)
            
            send_mail(
                email_title,
                email_message_bid,
                'admin@artifact-auction.com',
                [artifact.current_bidder.email],
                fail_silently=False,)
                         
            successful_bid = True
        else:
            messages.error(request,
                           "Your offer needs to be higher than the current bid")
    return successful_bid    
    
