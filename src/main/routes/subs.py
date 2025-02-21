from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.model.repositories.eventos_repository import EventosRepository
from src.main.use_cases.events_creator import EventsCreator  # Certifique-se de importar corretamente
from src.validators.events_creator_validator import events_creator_validator  # Se essa função existir

# Criando o Blueprint com o nome correto
subs_route_bp = Blueprint("subs_route", __name__)

@subs_route_bp.route("/subscriber", methods=["POST"])  # Corrigido de event_route_bp para subs_route_bp
def create_new_subs():
    # Validação da requisição
    events_creator_validator(request)
    
    # Criando um HttpRequest com o corpo da requisição
    http_request = HttpRequest(body=request.json)
    
    # Criando instâncias necessárias
    eventos_repo = EventosRepository()
    events_creator = EventsCreator(eventos_repo)
    
    # Chamando a função create apenas uma vez
    http_response = events_creator.create(http_request)
    
    # Retornando a resposta formatada
    return jsonify(http_response.body), http_response.status_code
