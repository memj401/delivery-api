from flask import jsonify
import repositorioPedidos

def inserir(dados):
    if not "cliente" in dados:
        return {"Erro": "Campo vazio (Cliente)"}, 400
    
    if not "produto" in dados:
        return {"Erro": "Campo vazio (Produto)"}, 400
    
    if not "valor" in dados:
        return {"Erro": "Campo vazio (Valor)"}, 400
    
    if  not isinstance(dados["valor"],float):
         return {"Erro": "Campo Valor não Válido"}, 400

    return jsonify(repositorioPedidos.inserir(dados)), 201

def atualizar(id, dados):
    if len(dados) == 0:
        return {"Erro": "Não há campos para serem editados"}, 400
    pedido_existe = repositorioPedidos.buscar(id)
    
    if not pedido_existe:
        return {"Erro": "Pedido não encontrado"}, 404
    
    if  "valor" in dados:
        if not isinstance(dados["valor"],float):
            return {"Erro": "Campo  Valor  não Válido"}, 400
    
    if  "entregue" in dados:
        if not isinstance(dados["entregue"], bool):
            return {"Erro": "Campo  Entregue  não Válido"}, 400
    

    return jsonify(repositorioPedidos.atualizar(id, dados)), 200

def atualizarStatusEntrega(id, dados):
    if len(dados) == 0 or not "entregue" in dados:
        return {"Erro": "Não há campos para serem editados"}, 400
    
    pedido_existe = repositorioPedidos.buscar(id)
    
    if not pedido_existe:
        return {"Erro": "Pedido não encontrado"}, 404

    if not isinstance(dados["entregue"], bool):
        return {"Erro": "Campo  Entregue  não Válido"}, 400
    

    return jsonify(repositorioPedidos.atualizarStatusEntrega(id, dados["entregue"])), 200

def deletar(id):
    pedido_existe = repositorioPedidos.buscar(id)

    if not pedido_existe:
        return {"Erro": "Pedido não encontrado"}, 404
    
    repositorioPedidos.deletar(id)

    return jsonify("Pedido Deletado")

def buscar(id):
    pedido_existe = repositorioPedidos.buscar(id)
    
    if not pedido_existe:
        return {"Erro": "Pedido não encontrado"}, 404
    
    return jsonify(pedido_existe)

def obterTotalGastoCliente(dados):
    if not "cliente" in dados:
        return {"Erro": "Campo vazio (Cliente)"}, 400
    total_gasto = repositorioPedidos.obterTotalGastoCliente(dados["cliente"])
    return jsonify({"Total Gasto": total_gasto})

def obterTotalGastoProduto(dados):
    if not "produto" in dados:
        return {"Erro": "Campo vazio (Produto)"}, 400
    total_gasto = repositorioPedidos.obterTotalGastoProduto(dados["produto"])
    return jsonify({"Total Gasto": total_gasto})

def listarMaisVendidos():
    lista_mais_vendidos = repositorioPedidos.listarMaisVendidos()
    if len(lista_mais_vendidos) == 0:
        return {"Erro": "Não há produtos cadastrados"}, 404
    return jsonify(lista_mais_vendidos)