from .models import shlModel
from .serializers import shlSerializer
from rest_framework import viewsets

class shlView(viewsets.ModelViewSet):
    queryset=shlModel.objects.all()
    serializer_class=shlSerializer 