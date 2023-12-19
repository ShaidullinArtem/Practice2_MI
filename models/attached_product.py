from dataclasses import dataclass


@dataclass
class AttachedProductModel:
    main_product_id: int
    attached_product_id: int
