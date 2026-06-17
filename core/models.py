from django.db import models
# Create your models here.



class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    
    Categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
    

class Pedidos(models.Model):
    nome_cliente = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_pedido = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome_cliente