from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from backoffice_demo_django.pii.models import Pii

def pii_detail_view(request):
    objs=Pii.objects.all()
    return render(request,'pii/pii.html',{'objs': objs})