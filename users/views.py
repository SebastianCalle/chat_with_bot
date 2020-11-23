"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Froms
from users.forms import NewUserForm


class LoginUserView(View):
    """View for login users."""

    def get(self, request):
        return render(request, template_name='users/login.html')

    def post(self, request):
        """Handle the POST request."""

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

        form = AuthenticationForm()
        return render(
            request=request,
            template_name="users/login.html",
            context={"login_form": form}
        )


class RegisterUserView(View):
    """View for register new users."""
    form_class = NewUserForm

    def get(self, request):
        return render(request=request, template_name='users/register.html')

    def post(self, request):
        """Handle request POST mehthod."""
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(
            request,
            "Unsuccessful registration. Invalid information."
        )
        form = NewUserForm

        return render(
            request=request,
            template_name="users/register.html",
            context={"register_form": form}
        )


def logout_users(request):
    """View for logout users."""
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("users:login")


class HomePageView(LoginRequiredMixin, View):
    """View home page """
    login_url = 'users/login'
    redirect_field_name = ''

    def get(self, request):
        context = {
            'user': request.user.username
        }
        return render(
            request,
            template_name='users/home.html',
            context=context
        )
