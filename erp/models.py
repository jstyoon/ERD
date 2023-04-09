from django.db import models


class Product(models.Model):
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('F', 'Free'),
    )
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    price = models.IntegerField()
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)

    def __str__(self):
        return self.code


class Stock(models.Model):
    """
    재고 모델입니다.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.quantity}"
