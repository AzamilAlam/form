from django.http import HttpResponse
from django.shortcuts import render


def index(request) :
    return render (request,"index.html")


def analyze(request):
    dtext=request.GET.get("text" ,"off")
    rpunc=request.GET.get("removepunc","deafault")
    fullcaps=request.GET.get("fullcaps","off")
    print(fullcaps)
    
    if rpunc == "on":
        # analyzed = dtext
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for i in dtext:
            if i not in punc:
                analyzed = analyzed + i
        paramas={"purpose" : "Removed Punctutations" , "analyzed_text" : analyzed}
        dtext = analyzed
        # return render(request,"analyze.html",paramas)
    
    if fullcaps == "on":
        analyzed = dtext.upper()
        params = {"purpose": "Capitalizing Your Text", "analyzed_text": analyzed}
        dtext=analyzed
    
    return render(request, "analyze.html", params)       

def capfirst(request):
    return HttpResponse("CapFirst")