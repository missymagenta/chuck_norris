import requests,json
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)

        joke = json_data.get("value").get("joke")

        context = {'joker': joke}

        return render(request,'namejoke/index.html',context)

    else:
        return render(request,'namejoke/index.html')
