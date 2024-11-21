from django.db import models
from django.contrib.auth.models import User

class CalculationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    expression = models.CharField(max_length=255)  # e.g., "7+8-3*2"
    result = models.CharField(max_length=255)      # e.g., "10"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expression} = {self.result} ({self.timestamp})"
