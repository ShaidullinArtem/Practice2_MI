from dataclasses import dataclass


@dataclass
class ProductPhotoModel:
    id: int
    product_id: int
    photo_path: str
