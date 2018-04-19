from django.conf import settings
from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from .models import *
from django.core.mail import send_mail

def contact(request):
    connected = False
    
    form = ContactForm()
    
    if request.method == 'POST':
        #print("hello, there")
        form = ContactForm(request.POST)
        
        
        if form.is_valid():
            #print("after form")
            form_email = form.cleaned_data["email_adress"]
            form_message = form.cleaned_data["message"]
            form_full_name = form.cleaned_data["full_name"]
            form_subject = form.cleaned_data["subject"]
            
            #template = get_template('contact_template.txt')
            #subject = request.POST.get('subject', '')
            
            subject = 'site contact form'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'lubwimi@hotmail.com']
            contact_message = "%s: %s via %s" %(
                form_full_name,
                form_message,
                form_email
            )
            
            send_mail(subject,
                      contact_message,
                      from_email,
                      to_email,
                      fail_silently=True # If you dont want to save in the db means dont work do False.
            )
            
            contact = Contact(full_name=form_full_name, email_adress=form_email, subject=form_subject, message=form_message)
            contact.save()
            
            connected = True
        else:
            pass
    else:
        form = ContactForm()
    
 
    context = {
        "form": form,
        "connected": connected
    }
            
            #content = template.render(context_dict)
            #
            #email = EmailMessage(
            #    "New contact form submission",
            #    content,
            #    "Your website" +'',     # My website
            #    ['lubwimi@gmail.com'],
            #    headers = {'Reply-To': email_adress },
            #)
            #email.send
            #return redirect('/contact/')
            
    return render(request, 'contact.html', context)
    
