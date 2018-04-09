from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Patmos
from .forms import PatmosForm, UserForm

# Create your views here.

def home(request):
    greeting = 'Medlemmar'
    
    #if request.method == 'POST':
    #    form = PatmosForm(request.POST)
    #    
    #    if form.is_valid():
    #        form.save()
    #        
    #        return medlem(request)
    #    else:
    #        form.errors
    #else:
    #    form = PatmosForm()
    #
    context = {
        'greeting': greeting,
        #'form': form,
    }
    
    return render(request, 'home.html', context)

def registform(request):
    register1 = 'Registrera Medlemar !'
    
    if request.method == 'POST':
        form = PatmosForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return medlem(request)
        else:
            form.errors
    else:
        form = PatmosForm()
    
    context = {
        'register1': register1,
        'form': form,
    }
    
    return render(request, 'registform.html', context)
    

def medlem(request):
    
    medlem_list = Patmos.objects.all()
    paginator = Paginator(medlem_list, 100) # Show 2 medlemmar per page
    
    page = request.GET.get('page')
    try:
        medlemmar = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        medlemmar = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        medlemmar = paginator.page(paginator.num_pages)
    
    context_dict = {
        'medlemmar': medlemmar, 
    }
    
    return render(request, 'medlem.html', context_dict)

def about(request):
    return render(request, 'about.html', {})

def search_medlem(request):
    if request.method == "POST":
        search_text = request.POST['search_text'] # ['search_text'] is a dictionary whose value will post by a user
    else:
        search_text = ''
    
    medlemmar = Patmos.objects.filter(fornamn__contains=search_text) # __contains is a method in django
    
    context = {
        'medlemmar': medlemmar,
    }
    
    return render(request, 'ajax_search.html', context)

def your_medlem(request, medlem_id=1): # if no medlem suplied in the form take the first one
    context_dict = {
        'your_medlem': Patmos.objects.get(id=medlem_id)
    }
    
    return render(request, 'your_medlem.html', context_dict)
    
def registeruser(request):
    registered = False # A boolean value for telling the template whether the registration was successful.Set to False initially. Code changes value to True when registration succeeds.
    
    if request.method == 'POST': 
        user_form = UserForm(data=request.POST) # Attempt to grab information from the raw form information.
        
        if user_form.is_valid():
            user = user_form.save() # Save the user's form data to the database.
            
            user.set_password(user.password) # Now we hash the password with the set_password method. Once hashed, we can update the user object.
            user.save()
            
            registered = True # Update our variable to tell the template registration was successful.
        else:
            print(user_form.errors) # Invalid form or forms - mistakes or something else? Print problems to the terminal. They'll also be shown to the user
        
    else:
        user_form = UserForm() # Not a HTTP POST, so we render our form using two ModelForm instances. This form will be blank, ready for user input.

    # Render the template depending on the context.
    return render(request, 'registuser.html', {'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password) # Use Django's machinery to attempt to see if the username/password combination is valid - a User object is returned if it is.
        
        if user:    # If we have a User object, the details are correct.
            
            if user.is_active:  # Is the account active? It could have been disabled.
                
                login(request, user)    # If the account is valid and active, we can log the user in. We'll send the user back to the homepage.
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Din inloggning kontot ar inaktivt. Kontakta Pastor ") # An inactive account was used - no logging in!
        else:
            print("Inkorekta inloggning detailjer: {0}, {1}".format(username, password)) # Bad login details were provided. So we can't log the user in.
            return HttpResponse("Inloggning uppgifter ar inkorrekta.")
    # The request is not a HTTP POST, so display the login form.
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)     #Since we know the user is logged in, we can now just log them out.
    
    return HttpResponseRedirect('/home/')   # Take the user back to the homepage.

def delete(request, medlem_id):
    try:
        obj = Patmos.objects.get(pk=medlem_id)
        obj.delete()
    except:
        pass
    
    return redirect("/medlem/")
    
    
    