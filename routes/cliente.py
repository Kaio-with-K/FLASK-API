from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
    - /clientes/ (GET) - Lista os clientes
    - /clientes/ (POST) - Insere o cliente no servidor
    - /clientes/new (GET) - Renderiza o formulário para criar um cliente
    - /clientes/<id> (GET) - Obtem um cliente pelo ID
    - /clientes/<id>/edit/ (GET) - renderiza o formulário para editar o cliente
    - /clientes/<id>/update/ (PUT) - Atualiza os dados do cliente
    - /clientes/<id>/delete/ (DELETE) - Deleta o registro do usuário
"""

@cliente_route.route('/')
def listar_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json
    new_user = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email']
    }
    
    CLIENTES.append(new_user)
    return render_template('item_cliente.html', cliente=new_user)

@cliente_route.route('/new')
def form_new_cliente():
    return render_template('form_clientes.html')

@cliente_route.route('/<int:id_cliente>')
def get_cliente_id(id_cliente):
    return render_template('get_clientes.html')

@cliente_route.route('/<int:id_cliente>/edit')
def form_cliente_id(id_cliente):
    cliente = None
    for c in CLIENTES:
        if c['id'] == id_cliente:
            cliente = c
    return render_template('form_clientes.html', cliente=cliente)

@cliente_route.route('/<int:id_cliente>/update', methods=['PUT'])
def update_cliente_id(id_cliente):
    cliente = None
    data = request.json
    
    for c in CLIENTES:
        
        if c['id'] == id_cliente:
            c['nome'] = data['nome']
            c['email'] = data['email']
            
            cliente = c
    return render_template('item_cliente.html', cliente=cliente)

@cliente_route.route('/<int:id_cliente>/delete', methods=['DELETE'])
def delete_cliente_id(id_cliente):
    global CLIENTES
    
    CLIENTES = [
        c for c in CLIENTES if c ['id'] != id_cliente
    ]
    
    return{ 'deleteded': 'ok'}