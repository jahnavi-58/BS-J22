from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company, IPOData
from .serializers import CompanySerializer, IPODataSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'sector']
    ordering_fields = ['name', 'founded_year', 'created_at']

class IPODataViewSet(viewsets.ModelViewSet):
    queryset = IPOData.objects.all()
    serializer_class = IPODataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['company__name', 'status']
    ordering_fields = ['open_date', 'close_date', 'listing_date', 'issue_size']