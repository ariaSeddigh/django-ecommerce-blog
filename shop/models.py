from django.db import models
from django.conf import settings
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_months = models.IntegerField()  # مثلا 1 ماه یا 3 ماه
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.subscription.name}"
