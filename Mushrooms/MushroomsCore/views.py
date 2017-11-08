import uuid

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .c12n import categories
from .forms.mushrooms.file_upload_form import FileForm
from .image_handler import handle_uploaded_file, handle_uploaded_bytearray


@csrf_exempt
def api_recognise(request):
    set_session_uuid(request)
    if request.method == 'POST':

        file_as_bytearray = request.body

        result = handle_uploaded_bytearray(file_as_bytearray, request.session['session_uuid'])

        params = {
            'result_name': result[0].name,
            'result_probability': float(result[0].probability)
        }

        return JsonResponse(params)
    else:
        return HttpResponse("You should send POST request with your file as bytearray in body")


def set_session_uuid(request):
    if request.session.get('session_uuid') is None:
        request.session['session_uuid'] = str(uuid.uuid4())


def index(request):
    set_session_uuid(request)
    if request.method == 'POST':

        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']

            result = handle_uploaded_file(file, request.session['session_uuid'])

            if result[0].probability < 0.6:
                params = {
                    'result_name': categories[result[0].name] + " или " + categories[result[1].name],
                    'result_probability': str(round(result[0].probability * 100, 2)) + " и " +
                                          str(round(result[1].probability * 100, 2))
                }
            else:
                params = {
                    'result_name': categories[result[0].name],
                    'result_probability': round(result[0].probability * 100, 2)
                }

            return render(request, 'mushrooms/thanks.html', params)

    else:
        form = FileForm()

        return render(request, 'mushrooms/index.html', {'form': form})
