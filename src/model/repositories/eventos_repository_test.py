import pytest
from src.model.repositories.eventos_repository import EventosRepository


@pytest.mark.skip("Insert in DB")
def test_insert_eventos():
    event_name = "SubSub"
    event_repo = EventosRepository()
    
    event_repo.insert(event_name)
    
def test_select_event():
    event_repo = EventosRepository()
    event_name = "SubSub"
    
    event = event_repo.select_event(event_name)
    print(event)
    print(event.nome)
        
