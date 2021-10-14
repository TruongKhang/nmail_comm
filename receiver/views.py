from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import ModelFile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser


# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


@method_decorator(csrf_exempt, name='dispatch')
class Receiver(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file_type = request.data["type"]
        file_field = request.data["file"]
        instance = ModelFile(file_type=file_type, file_field=file_field)
        instance.save()
        # form = ModelFormWithFileField(instance=instance)
        # form.save()
        response = {
            "filetype": file_type,
            "filename": instance.file_field.name,
            "message": "Receiving file successfully!"
        }
        return JsonResponse(response, status=201)

