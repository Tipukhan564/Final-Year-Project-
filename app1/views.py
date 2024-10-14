from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login  # Optional: for logging in the user after signup

# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        # Fetch data from the form
        first_name = request.POST.get('name')  # Assuming name field is the first name
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        # Validate if both passwords match
        if password1 == password2:
            # Create the user in the User model
            my_user = User.objects.create_user(username=username, password=password1, email=email)
            my_user.first_name = first_name  # Assuming no separate field for last_name
            my_user.save()

            # Optionally log the user in after signup
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)

            return HttpResponse("User has been created successfully!")
        else:
            return HttpResponse("Passwords do not match!")
    
    return render(request, 'signup.html')


