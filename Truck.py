from dataclasses import dataclass

@dataclass
class Truck: 
	ID: int
	code: int
	startLocation: str
	destination: str
	latitude: float
	longitude: float
	
