#I have created this file - safi
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    punctuations = '''/.,/.,';';][]*//-*''"";::-@!#$%^&**(()~``'''
    #Check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Double Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if charactercounter == "on":
        analyzed = ""
        count = 1
        for char in djtext:
            if char !=" " and char !='\n':
                analyzed = count
                count += 1
        params = {'purpose': 'Total Characters', 'analyzed_text': analyzed}

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover != "on" and charactercounter!="on"):
        return  HttpResponse('Error')

    return render(request, 'analyze.html', params)
