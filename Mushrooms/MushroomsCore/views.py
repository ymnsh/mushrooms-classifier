from .forms.mushrooms.file_upload_form import FileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .ziga import handle_uploaded_file


def index(request):
    if request.method == 'POST':
        # Обработка тут
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            result = handle_uploaded_file(request.FILES['file'])

            return render(request, 'mushrooms/thanks.html', {'result': result})

    else:
        form = FileForm()

    return render(request, 'mushrooms/index.html', {'form': form})
