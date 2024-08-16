from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View

class RegistrationPage(View):
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        
        if uname and email and pass1:
            try:
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                my_user.save()
                return redirect(self.success_url)
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
        else:
            return HttpResponse("Username, email, and password are required.")
        
class LoginPage(View):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect()
        else:
            return HttpResponse("Username or Password is incorrect!!!")

class LogoutPage(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class DashboardView(View):
    def post(self, request, *args, **kwargs):
        return render('login')

"""
class AddMember(View):

class ShowMembers(View):

class CreateGroup(View):

class EditGroup(View):

class DeleteGroup(View):

class InviteMember(View):

class CreateExpense(View):

class DeletExpense(View):

class EditExpense(View):

class Settlement(View);
"""

