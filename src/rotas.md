- *url_base* = *http://localhost:5000* (Rota base da Aplicação)
- *url_base/pedido*: Rota utilizada para cadastro de um novo pedido na base de dados. 

Formato da Requisição:
```
HTTP METHOD: POST
{
	"cliente": String ,
	"produto": String,
	"valor":Float
}  
```

- *url_base/ \<id>* : Rota utilizada para modificação,busca ou remoção das informações de um pedido da base de dado, especificado pelo campo id na rota. A seleção do serviço é realizada pelo metódo HTTP da Requisição. 

Formato da Requisição (Modificação do Pedido):

 ```
 HTTP METHOD: PUT
{
 
	"cliente": String ,
	"produto": String,
	"valor": Float,
 "entregue" : Boolean
}  
```
 
Formato da Requisição (Busca do Pedido):

 ```
 HTTP METHOD: GET
{} # Requisição sem Corpo  
```
 
Formato da Requisição (Remoção do Pedido):

 ```
 HTTP METHOD: DELETE
{} # Requisição sem Corpo  
```
- *url_base/pedido/<id>/status*: Rota utilizada para modificação dos status de entrega de um produto da bae de dados, especificado pelo campo id da rota.
 
 Formato da Requisição:

 ```
 HTTP METHOD: PUT
{"entregue" : Boolean}  
```
 
 - *url_base/total_gasto/cliente*: Rota utilizada para obtenção do gasto total de todos os pedidos entregues de um cliente em específico.
 
 Formato da Requisição:

 ```
 HTTP METHOD: GET
{"cliente": String }  
```
 
 - *url_base/total_gasto/produto*: Rota utilizada para obtenção do gasto total de todos os pedidos entregues de um produto em específico.
 
 Formato da Requisição:

 ```
 HTTP METHOD: GET
{"produto": String }  
```
 
 - *url_base/lista_mais_vendidos*: Lista os produtos mais vendidos, em ordem decrescente do número de vendas.
 
 Formato da Requisição:

 ```
 HTTP METHOD: GET
{} # Requisição sem Corpo  
```