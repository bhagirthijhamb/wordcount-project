from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')

def bananas(request):
    # return HttpResponse('Bananas are great!')

    # not recommended. Should separate HTML code from the view code
    return HttpResponse('<h2>Bananas are great!</h2>')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    # return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': worddictionary})
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')