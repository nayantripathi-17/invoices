from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    invoice = models.AutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.invoice)    


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='details')
    description = models.TextField(null = False, blank = False)
    quantity = models.PositiveIntegerField(null = False, blank = False, default = 1)
    unit_price = models.DecimalField(null = False, blank = False, default = 0.0, max_digits=10, decimal_places=2)
    price = models.DecimalField(blank = True,max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id) 
    
    def save(self, *args, **kwargs):
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

