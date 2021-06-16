from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.

monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'Leand python for at least 20 minutes every day',
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f'<ul>{list_items}</ul>'

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    reverse_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):
    try:
        challeng_text = monthly_challenges[month]
        challeng_data = f'<h1>{challeng_text}</h1>'
        return HttpResponse(challeng_data)
    except:
        return HttpResponseNotFound('This month is not supported')
