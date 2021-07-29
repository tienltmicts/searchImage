from django.shortcuts import render, redirect
from .colordescriptor import ColorDescriptor
from .searcher import Searcher
import argparse
import cv2
import glob
from .models import Image
from .forms import ImageForms

# Create your views here.
def search(request):
    respone = []
    image =''
    if request.method == 'POST':
        form = ImageForms(request.POST, request.FILES)
        
        if form.is_valid():
            if  'id_selfie' in request.FILES :
                query_image = request.FILES.get('id_selfie')
                image = Image.objects.create(id_selfie=query_image)
                image.save()

                cd = ColorDescriptor((8, 12, 3))
                #load the query image and describe it
                s = image.id_selfie.url
                query = cv2.imread(s[1:])
               
                features = cd.describe(query)
                # perform the search
                searcher = Searcher('search/static/index.csv')
                results = searcher.search(features)
               
                # display the query
                for (score, resultID) in results:
                    print(resultID)
                    respone.append( "../static/"+resultID)
                        # image = cv2.imread(imagePath)
                        # cv2.imshow("Result" + str(i), image)
    else:
        form = ImageForms()

    return render(request, 'search.html', {'form' : form, 'result': respone, 'query': image})

   