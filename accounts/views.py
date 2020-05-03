from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import RegisterForm

# Create your views here.

# test view
def test_view(request):
    context = {
        "message" : "welcome",
    }
    return render(request, "accounts/test_template.html", context)


@csrf_exempt
def register_view(request):
    """View to handle registration

    If the client uses a GET request, display the HTML page for registration
    that includes the registration form.

    If the client uses a POST request, validate the data, create a User, and
    redirect to the home page.
    """
    # TODO: remove "@csrf_exempt" after figuring out what it does
    if request.method == 'GET':
        context = {'form': RegisterForm()}
        return render(request, 'accounts/register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if not form.is_valid():
            context = {'form':form}
            return render(request, 'accounts/register.html', context)

        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Check if a user already exists with that username
        try:
            user= User.objects.get(username=username)
            context = {'form':form, 'error': f'The username {username} is already taken'}
            return render(request, 'accounts/register.html', context)
        except User.DoesNotExist:
            # Create user and log them in
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return HttpResponseRedirect('/')

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])