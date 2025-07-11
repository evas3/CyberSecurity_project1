from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


def frontPage(request):
	return render(request, 'pages/frontpage.html')

def logIn(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		# Fix 2
		"""
		login_user = authenticate(request, username=username, password=password)
		if login_user is not None:
			login(request, login_user)
			return render(request, 'pages/user.html')
		"""
		
		if User.objects.filter(username=username, password=password).exists():
			return render(request, 'pages/user.html')
		
		else:
			return render(request, 'pages/login.html', {'error': 'Wrong username or password'})
	else:
		return render(request, 'pages/login.html')

def signUp(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		if password1 != password2:
			return render(request, 'pages/signup.html', {"error": "Passwords don't match"})
		
		if username == password1:
			return render(request, 'pages/signup.html', {"error": "Password can't be same as username"})
		
		# Fix 4
		"""
		signup_user = User(username=username)
		try:
			validate_password(password2, user=signup_user)
		except ValidationError as error:
			return render(request, 'pages/signup.html', {"error": error.messages[0]})
		"""

		if User.objects.filter(username=username).exists():
			return render(request, 'pages/signup.html', {'error': 'Username already taken'})

		User.objects.create(
            username=username,
            password=password2
        )

		# Fix 2
		"""
		User.objects.create_user(
            username=username,
            password=password2
        )
		"""
		
		return render(request, 'pages/login.html', {'success': 'User created'})

	else:
		return render(request, 'pages/signup.html')

# Fix 6
"""
@login_required(login_url="/login")
"""

def loggedUser(request):
	return render(request, 'pages/user.html')

#@login_required(login_url="/home")
def logOut(request):

	# Fix 6
	"""
	try:
		logout(request)
	except:
		pass
	"""

	return render(request, 'pages/frontpage.html')