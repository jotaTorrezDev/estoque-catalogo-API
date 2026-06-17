from rest_framework import serializers
from .models import Produto, Categoria, Pedidos


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']



class ProdutoSerializer(serializers.ModelSerializer):
        Categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

        class Meta:
            model = Produto
            fields = ['id', 'nome', 'preco', 'estoque', 'Categoria']


class PedidosSerializer(serializers.ModelSerializer):
    produtos = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True)

    class Meta:
        model = Pedidos
        fields = ['id', 'nome_cliente', 'email_cliente', 'data_pedido', 'produtos']