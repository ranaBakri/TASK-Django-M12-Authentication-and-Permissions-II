from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout


def user_register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("home")
    context = {
        "form": form,
    }

    return render(request, "regester.html", context)


def signup(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_passward(user.passward)
            user.save()
            return redirect("item_list")
    context = {"form": form}
    return render(request, "signup.html", context)


def signout(request):
    logout(request)
    return redirect("regester")
