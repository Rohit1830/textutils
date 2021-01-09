# #created by me- Rohit
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
    
#     return render(request,'index.html')
# def analyze(request):
#     #get the text
#     djtext = (request.POST.get('text', 'default'))

#     #check checkbox values
#     removepunc= request.POST.get('removepunc', 'off')
#     capitalize= request.POST.get('capitalize', 'off')
#     RemoveExtraSpace = request.POST.get('RemoveExtraSpace', 'off')
#     analyzed = ''
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
#     if removepunc == 'on':
        
#         for ele in djtext:  
#             if ele not in punctuations:  
#                 analyzed = analyzed + ele
        
#         params = {'purpose' : 'remove punctuations', 'analyzed_text':analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
    
#     if capitalize == 'on':
#         analyzed= djtext.upper()
#         params = {'purpose' : 'Capitalize all', 'analyzed_text':analyzed}
#         # return render(request, 'analyze.html', params)
#         djtext= analyzed

#     if RemoveExtraSpace == 'on':
#         for index, char in enumerate(djtext):
#             if not (djtext[index]== " " and djtext[index + 1] == " "):
#                 analyzed = analyzed+char
#         params = {'purpose' : 'Remove extra space', 'analyzed_text':analyzed}
    
#     if(removepunc!="on" and RemoveExtraSpace!="on" and capitalize!="on"):
#         return HttpResponse("turn on analyzer")
    
#     return render(request, 'analyze.html', params)
#         # djtext=analyzed

#         # else:
#     #     return HttpResponse("Turn on analyzer")

# # def removepunc(request):
# #     djtext = (request.GET.get('text', 'default'))
# #     print(djtext)
# #     return HttpResponse('''removepunc''')
    

# # def capfirst(request):
# #     return HttpResponse(''' capfirst ''')

# # def newlineremove(request):
# #     return HttpResponse(''' newlineremove ''')

# # def spaceremove(request):
# #     return HttpResponse('''spaceremove''')

# # def charcount(request):
# #     return HttpResponse(''' charcount ''')

# I have created this file - Harry video #17
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''For Entertainment youtube video''',
             '''For Interaction Facebook''',
             '''For Insight   Ted Talk''',
             '''For Internship   Intenship''',
             ]
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(capitalize=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed extra space', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and capitalize!="on" and numberremover!= "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)




