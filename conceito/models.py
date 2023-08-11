from django.db import models

    
class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Camiseta(models.Model):
    descricao = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="marca")
    tamanho = models.CharField(max_length=4)
    valor = models.DecimalField(default="R$", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao