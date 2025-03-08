from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logos/')
    description = models.TextField()
    sector = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class IPOData(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('listed', 'Listed'),
    ]

    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='ipo_data')
    price_band_low = models.DecimalField(max_digits=10, decimal_places=2)
    price_band_high = models.DecimalField(max_digits=10, decimal_places=2)
    issue_size = models.DecimalField(max_digits=15, decimal_places=2)  # In crores
    min_lot_size = models.PositiveIntegerField()
    open_date = models.DateField()
    close_date = models.DateField()
    listing_date = models.DateField(null=True, blank=True)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')
    rhp_document = models.FileField(upload_to='documents/rhp/', null=True, blank=True)
    drhp_document = models.FileField(upload_to='documents/drhp/', null=True, blank=True)
    subscription_retail = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_qib = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subscription_nii = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "IPO Data"
        ordering = ['-open_date']

    def __str__(self):
        return f"{self.company.name} IPO"

    @property
    def returns(self):
        if self.listing_price and self.current_price:
            return ((self.current_price - self.listing_price) / self.listing_price) * 100
        return None