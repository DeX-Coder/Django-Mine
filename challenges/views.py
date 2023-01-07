from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january":"Eat no meat this month",
    "february":"Walk for at least 20 mins every day!",
    "march":"Learn Django for at least 20mins everyday!",
    "april":"Eat no meat this month",
    "may":"Walk for at least 20 mins every day!",
    "june":"Eat no meat this month",
    "july":"Learn Django for at least 20mins everyday!",
    "august":"Walk for at least 20 mins every day!",
    "september":"Learn Django for at least 20mins everyday!",
    "october":"Eat no meat this month",
    "november":"Walk for at least 20 mins every day!",
    "december":"Learn Django for at least 20mins everyday!",
}

# Create your views here.

def monthly_challenges_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > 12:
        return HttpResponseNotFound("Invalid Month!")
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)