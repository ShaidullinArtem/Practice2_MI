from dataclasses import dataclass


@dataclass
class DocumentByServiceModel:
    id: int
    client_service_id: int
    document_path: str
