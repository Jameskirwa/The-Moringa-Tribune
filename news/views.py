from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Moringa Tribune")

def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(date):
    
    #functin that gets the weekday number for dates
    day_number = dt.date.weekday(date)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    # Returning the actual day of the week
    day = days[day_number]
    return day

def news_of_day(request):
    date = dt.date.today()
    # function to convert date object to find the exact day
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
    