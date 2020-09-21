# i have created this file - Ali
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    uppercasee = request.GET.get('uppercasee', 'off')
    lowerca = request.GET.get('lowerca', 'off')
    findnum = request.GET.get('findnum', 'off')

    #fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed


    #code
    if (uppercasee == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text

    if (lowerca == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()

        params = {'purpose': 'Changed to lowercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        return render(request, 'analyze.html', params)

    #
    else:
        return HttpResponse('error')



def about(request):
    return render(request,'about.html')


# def html1(request):
#     djtext=request.GET.get('text','default')
# def about(request):
#     return HttpResponse("'<h1> About us </h1>  <a href='menu'> back </a> ")
#
# def menu(request):
#     return HttpResponse("<h1>Here if our menus</h1>  <a href='links'> back to links </a> <br> <a href='about'> back to about </a> <br> <a href='html1'> back to html1 </a>")
#
# def links(request):
#     return HttpResponse(' ' '<h1> Here is our links <h1> <a href="https://www.w3schools.com">Visit W3Schools</a> ' ' ')
# def links1(request):
#     return HttpResponse(' ' '<h1> Here is our links1 <h1> <a href="https://google.com">Visit W3Schools</a> ' ' ')




