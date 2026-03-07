from dataclasses import dataclass


@dataclass
class Repository:
    name: str
    description: str
    private: bool = False