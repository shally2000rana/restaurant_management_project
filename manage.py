#in your models.py file(assuming a Django-like structure)
class Restaurant(models.Model):
    operaating_days=models.CharField(
        max_length=50,
        blank=True,
        default=",
        help_text="Comma-separated list of operating days"
    )

