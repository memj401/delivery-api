from flask import Blueprint, request
import controladoraPedidos

url = Blueprint('url',__name__)

@url.route('/pedido', methods = ["POST"])
def criar_pedidos():
    if request.method == "POST":
        return controladoraPedidos.inserir(request.json)

@url.route('/pedido/<id>', methods = ["PUT","DELETE","GET"])
def acessar_pedido(id):
    if request.method == "PUT":
        return controladoraPedidos.atualizar(int(id), request.json)
    if request.method == "DELETE":
        return controladoraPedidos.deletar(int(id))
    if request.method == "GET":
        return controladoraPedidos.buscar(int(id))

@url.route('/pedido/<id>/status', methods = ["PUT"])
def acessar_pedido_status(id):
    if request.method == "PUT":
        return controladoraPedidos.atualizarStatusEntrega(int(id), request.json)

@url.route('/total_gasto/cliente', methods = ["GET"])
def obter_total_gasto_por_cliente():
    if request.method == "GET":
        return controladoraPedidos.obterTotalGastoCliente(request.json)

@url.route('/total_gasto/produto', methods = ["GET"])
def obter_total_gasto_por_produto():
    if request.method == "GET":
        return controladoraPedidos.obterTotalGastoProduto(request.json)

@url.route('/lista_mais_vendidos', methods = ["GET"])
def obter_lista_mais_vendidos():
    if request.method == "GET":
        return controladoraPedidos.listarMaisVendidos()