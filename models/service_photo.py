from dataclasses import dataclass


@dataclass
class ServicePhotoModel:
    id: int
    service_id: int
    photo_path: str
