from django.shortcuts import render

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import ProjectMaster
from .serializer import ProjectMasterSerializer


class ProjectListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ProjectMaster.objects.all()
    serializer_class = ProjectMasterSerializer

class ProjectSetPagenation(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
