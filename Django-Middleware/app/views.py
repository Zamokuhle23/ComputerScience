from django.shortcuts import render, HttpResponse


def Home(request):
    print("Middleware Here Completed!!!")
    return HttpResponse("Home Page But is Empty")
