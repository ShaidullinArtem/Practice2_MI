from dataclasses import dataclass


@dataclass
class ProductModel:
    id: int
    title: str
    cost: float
    description: str
    main_image_path: str
    is_active: bool
    manufacturer_id: int
