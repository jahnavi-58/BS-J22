from rest_framework import serializers
from .models import Company, IPOData

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class IPODataSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_logo = serializers.ImageField(source='company.logo', read_only=True)
    returns = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = IPOData
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')