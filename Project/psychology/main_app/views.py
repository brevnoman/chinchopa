from django.shortcuts import render, redirect
# from main_app.forms import NewUserForm
# from django.contrib.auth import login
# from django.contrib import messages


def render_main_page(request):
    return render(request, "main_page.html")


def sing_in_page(requset):
    return render(requset, "Sing_in.html")

def register_page(request):    #на моменте попытки подключения view появляется ошибка о том что приложение не зарегистрировано
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Registration successful.")
    #         return redirect("")
    #     messages.error(request, "Unsuccessful registration. Invalid information.")
    # form = NewUserForm()
    # return render(request, "register.html", context={"register_form": form})
    return render(request, "register.html")