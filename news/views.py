from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render
from .forms import NewsLetterForm
from django.http import JsonResponse
from .email import send_welcome_email
from .models import *
# Create your views here.
def subscribe(request):
#........
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            data = {'success': 'You have been successfully added to mailing list'}
            return JsonResponse(data)

            # HttpResponseRedirect('subscribe.html')
    else:
        form = NewsLetterForm()
    return render(request, 'subscribe.html', {"letterForm":form})