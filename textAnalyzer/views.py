from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Getting the text with POST.get
    # Did not used GET.get Because of security
    # 'text' from the textarea of the form
    text = request.POST.get('text','default')

    # For removing punctuations
    rmvpunc = request.POST.get('rmvpunc','off')
    # For all capital letters
    capltr = request.POST.get('capltr','off')
    # For new line removing
    nlrmv = request.POST.get('nlrmv','off')
    # For extra space removing
    exspcrmv = request.POST.get('exspcrmv','off')
    # For number removing
    numrmv = request.POST.get('numrmv','off')

    # For removing punctuations
    if rmvpunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        # Analyzed text
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        text = analyzed

    # For all capital letters
    if capltr == 'on':
        analyzed = ''
        for char in text:
            analyzed += char.upper()
        params = {'purpose' : 'Capitalized', 'analyzed_text' : analyzed}
        text = analyzed

    # For new line removing
    if nlrmv == 'on':
        analyzed = ''
        for char in text:
            if char!= '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'New Line removed', 'analyzed_text': analyzed}
        text = analyzed

    # For extra space removing
    if exspcrmv == 'on':
        analyzed = ''
        for index, char in enumerate(text):
            if char == text[-1]:
                if not (text[index] == ' '):
                    analyzed += char
            elif not(text[index] == ' ' and text[index+1] == ' '):
                analyzed += char
        params = {'purpose': 'Extra space remove', 'analyzed_text': analyzed}
        text = analyzed

    # For number removing
    if numrmv == 'on':
        analyzed = ''
        numbers = "0123456789"
        for char in text:
            if char not in numbers:
                analyzed += char
        params = {'purpose': 'Number Removed', 'analyzed_text': analyzed}
        text = analyzed

    # For invalid input
    if(rmvpunc!='on' and capltr!='on' and exspcrmv!='on' and nlrmv!='on' and numrmv!='on'):
        return HttpResponse("Select any operation and try again")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')