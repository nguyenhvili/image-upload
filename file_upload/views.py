from django.contrib import messages
from django.http import FileResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from file_upload.decorators import login_required
import datetime
import os


# @login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    elif request.method == "POST":
        # validation
        if not request.FILES.get('file'):
            messages.error(request, 'Vyberte prosím soubor')
            return HttpResponseBadRequest()
            # return redirect('create')

        file = request.FILES['file']

        # file_extension = ''
        # for i in ALLOWED_EXTENSIONS:
        #     if file.name.endswith(i):
        #         file_extension = i
        # if file_extension == '':
        #     messages.error(request, 'Formát není podporován')
        #     return HttpResponseBadRequest()

        film_url = "static/ahoj.png"
        f = open(film_url, 'wb+')
        for chunk in file.chunks():
            f.write(chunk)

        # Photo.objects.create(
        #     name=request.POST['name'],
        #     description=request.POST.get('description'),
        #     csfd_link=request.POST['csfd_link'],
        #     csfd_description=csfd_description,
        #     csfd_rating=csfd_rating,
        #     author=request.user,
        #     film_url=film_url,
        #     extension=file_extension,
        #     size=os.stat(file_path + film_url).st_size
        # )
        messages.success(request, 'Film byl přidán')
        return HttpResponse("pridano")
