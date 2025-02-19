from src.model.entities.inscritos import Inscritos 
from abc import ABC, abstractmethod

class SubscribersRepository(ABC):
    @abstractmethod
    def insert(self, subscriber_infos: dict) -> None: pass
     
    @abstractmethod
    def select_subscriber(self, email: str, event_id: int) -> Inscritos: pass

