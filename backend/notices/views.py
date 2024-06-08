# notices/views.py
from rest_framework import viewsets
from .models import Notice
from .serializers import NoticeSerializer
from rest_framework.pagination import PageNumberPagination

class NoticePagination(PageNumberPagination):
    page_size = 10

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-created_at')
    serializer_class = NoticeSerializer
    pagination_class = NoticePagination