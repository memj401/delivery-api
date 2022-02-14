import json
from datetime import datetime

def inserir(dados):
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        novo_pedido = {
            "id" : pedidos_registrados["nextId"], 
            "cliente" : dados["cliente"], 
            "produto": dados["produto"],
            "valor": dados["valor"],
            "entregue": False,
            "timestamp": datetime.utcnow().isoformat() + 'Z'
        }
        pedidos_filtrados.append(novo_pedido)
        pedidos_registrados["nextId"] += 1
        pedidos_registrados["pedidos"] = pedidos_filtrados
        pedidos.close()
    with open("pedidos.json","w", encoding = "utf-8") as pedidos:
        json.dump(pedidos_registrados,pedidos, indent = 4, ensure_ascii = False)
        pedidos.close()
    return novo_pedido

def buscar(id):
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        pedido_existe = next((pedido for pedido in pedidos_filtrados if pedido["id"] == id), None)
    pedidos.close()
    return pedido_existe

def atualizar(id,dados):
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        pedidos.close()
    for i in range(len(pedidos_filtrados)):
        if pedidos_filtrados[i]["id"] == id:
            parametros = ["cliente","produto","valor","entregue"]
            for parametro in parametros:
                if parametro in dados:
                    pedidos_filtrados[i][parametro] = dados[parametro]
    
    pedidos_registrados["pedidos"] = pedidos_filtrados
    
    with open("pedidos.json","w", encoding = "utf-8") as pedidos:
       json.dump(pedidos_registrados,pedidos, indent = 4, ensure_ascii = False)
       pedidos.close() 
    
    return buscar(id)

def atualizarStatusEntrega(id,status):
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        pedidos.close()
    for i in range(len(pedidos_filtrados)):
        if pedidos_filtrados[i]["id"] == id:
            pedidos_filtrados[i]["entregue"] = status
    
    pedidos_registrados["pedidos"] = pedidos_filtrados
    
    with open("pedidos.json","w", encoding = "utf-8") as pedidos:
       json.dump(pedidos_registrados,pedidos, indent = 4, ensure_ascii = False)
       pedidos.close()
    return buscar(id)

def deletar(id):
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        pedidos.close()
    for i in range(len(pedidos_filtrados)):
        if pedidos_filtrados[i]["id"] == id:
            del pedidos_filtrados[i]
            break
    pedidos_registrados["pedidos"] = pedidos_filtrados
    
    
    with open("pedidos.json","w", encoding = "utf-8") as pedidos:
       json.dump(pedidos_registrados,pedidos, indent = 4, ensure_ascii = False)
       pedidos.close()

def obterTotalGastoCliente(cliente):
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        pedidos.close()
    
    total_gasto = 0.0
    for pedido in pedidos_filtrados:
        if "cliente" in pedido:
            if pedido["cliente"] == cliente and pedido["entregue"] == True:
                total_gasto += pedido["valor"]
    
    return round(total_gasto,2)

def obterTotalGastoProduto(produto):
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        pedidos.close()
    
    total_gasto = 0.0
    for pedido in pedidos_filtrados:
        if "produto" in pedido:
            if pedido["produto"] == produto and pedido["entregue"] == True:
                total_gasto += pedido["valor"]

    return round(total_gasto,2)

def listarMaisVendidos():
    with open("pedidos.json","r", encoding = "utf-8") as pedidos:
        pedidos_registrados = json.load(pedidos)
        pedidos_n_nulos = list(filter(lambda pedido: (pedido != None)  , pedidos_registrados["pedidos"]))
        pedidos_filtrados = list(filter(lambda pedido: (not isinstance(pedido["id"], float))  , pedidos_n_nulos))
        pedidos.close()
    lista_mais_vendidos = []
    copunt = 1
    for pedido in pedidos_filtrados:
        if len(lista_mais_vendidos) == 0:
            item = {"produto" : pedido["produto"], "quantidade_de_pedidos": 1}
            lista_mais_vendidos.append(item)
        else:
            produto_foi_inserido = False
            for i in range(len(lista_mais_vendidos)):
                if pedido["produto"]  in lista_mais_vendidos[i].values() and pedido["entregue"] == True:
                    lista_mais_vendidos[i]["quantidade_de_pedidos"] += 1
                    produto_foi_inserido = True
                    break
            if not produto_foi_inserido and pedido["entregue"] == True:
                item = {"produto" : pedido["produto"], "quantidade_de_pedidos": 1}
                lista_mais_vendidos.append(item)
    lista_mais_vendidos = sorted(lista_mais_vendidos, key = lambda pedido: pedido["quantidade_de_pedidos"],reverse=True)
    return lista_mais_vendidos