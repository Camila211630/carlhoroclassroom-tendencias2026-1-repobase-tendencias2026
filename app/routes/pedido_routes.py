from flask import Blueprint
from app.Controller.PedidoController import PedidoController

pedido_bp = Blueprint('pedido', __name__)

pedido_bp.route('/pedido', methods=['POST'])(PedidoController.crear)
