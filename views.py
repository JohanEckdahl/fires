
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from django.views.generic.edit import CreateView
from django.views import generic
from django.utils import timezone
from django.conf import settings

from .models import Fire
from .tables import FireTable, SkogsstyrelsenTable


def fires(request):
	table = FireTable(Fire.objects.all(), order_by="OBJECTID")
	RequestConfig(request, paginate=False,).configure(table)
	return render(request, 'fires/fires.html', {'table': table})

def skogsstyrelsen(request):
    table = SkogsstyrelsenTable(Fire.objects.all(), order_by="OBJECTID")
    RequestConfig(request, paginate=False,).configure(table)
    return render(request, 'fires/fires.html', {'table': table})
