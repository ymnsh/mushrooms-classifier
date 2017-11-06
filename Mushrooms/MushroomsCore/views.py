import uuid

from django.http import JsonResponse
from django.shortcuts import render

from .c12n import categories
from .forms.mushrooms.file_upload_form import FileForm
from .image_handler import handle_uploaded_file


def api_recognise(request):
    if request.method == 'POST':  # byte-array
        file = request.FILES['file']

        result = handle_uploaded_file(file, request.session['session_uuid'])

        params = {
            'result_name': result.name,
            'result_probability': float(result.probability)
        }

        return JsonResponse(params)


def index(request):
    if request.session.get('session_uuid') is None:
        request.session['session_uuid'] = str(uuid.uuid4())

    if request.method == 'POST':

        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']

            result = handle_uploaded_file(file, request.session['session_uuid'])

            params = {
                'result_name': categories[result.name],
                'result_probability': round(result.probability * 100, 2)
            }

            return render(request, 'mushrooms/thanks.html', params)

    else:
        form = FileForm()

        return render(request, 'mushrooms/index.html', {'form': form})
