from django.db import models

class NutritionalInformation(models.Model):
    menu_item=models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    calories=models.IntegerField()
    protein_grams=models.DecimalField(max_digits=5, decimal_places=2)
    fat_grams=models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate_grams=models.DecimalField(max_digits=5, decimal_places=2)
    def__str__(self):
        return f"{self.menu_item.name} - {self.calories} kcal"
        
         
