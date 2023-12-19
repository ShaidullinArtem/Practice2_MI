from dataclasses import dataclass


@dataclass
class TagModel:
    id: int
    title: str
    color: str
