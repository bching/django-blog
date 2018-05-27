# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.views.generic.edit import CreateView

class ContactView(CreateView):
    template_name = 'email.html'
    form_class = ContactForm()

# Non-AJAX method which causes a page reload
# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "email.html", {'form': form})
#
# def successView(request):
#     return HttpResponse('Success! Thank you for your message. :)')
