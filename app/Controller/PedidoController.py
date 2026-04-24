from flask import request, jsonify
from app.models.domain.service.Crear_pedido import crear_pedido

class PedidoController:
    @staticmethod
    def crear():
        data = request.get_json()
        clienteId = data.get('clienteId')
        productos = data.get('productos')
        if not clienteId or not productos:
            return jsonify({'mensaje': 'Faltan datos requeridos'}), 400
        try:
            pedido = crear_pedido(clienteId, productos)
            return jsonify(pedido), 201
        except Exception as e:
            return jsonify({'mensaje': 'Error al crear el pedido'}), 500
