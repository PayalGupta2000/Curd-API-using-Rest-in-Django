from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)

    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    description=models.TextField()
    image=models.URLField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        ordering=['id']

    def __str__(self):
        return '{} {}'.format(self.name,self.price)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        