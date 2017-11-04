from django.shortcuts import render
from django.http import JsonResponse
from .forms.mushrooms.file_upload_form import FileForm
from .image_handler import handle_uploaded_file
from .c12n import categories


def index(request):
    if request.method == 'POST':

        form = FileForm(request.POST, request.FILES)

        file = request.FILES['file']

        result = handle_uploaded_file(file)

        # Запрос с web-клиента
        if form.is_valid():

            params = {
                'result_name': categories[result.name],
                'result_probability': round(result.probability * 100, 2)
            }

            return render(request, 'mushrooms/thanks.html', params)

        # Запрос с иного клиента
        else:
            return JsonResponse(result.as_dict())

    else:
        form = FileForm()

    return render(request, 'mushrooms/index.html', {'form': form})
