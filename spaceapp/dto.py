from dataclasses import dataclass


@dataclass
class InputDTO:
    name: str
    font: str


@dataclass
class OutputDTO:
    name: str
    font: str
