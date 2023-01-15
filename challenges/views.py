from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december":None
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months":months,
    })

def monthly_challenges_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > 12:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', context={
            'month':month,
            'challenge':challenge_text
        })
    except:
        raise Http404()