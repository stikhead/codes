from dataclasses import dataclass

@dataclass(frozen=True)
class DBConfig:
    host: str
    port: str # these are hints for developers / IDES, they are not strictly enforced 
    # but fastapi upgrades dataclasses to strictly enforce these types and crash if it doesnt match

prod_db = DBConfig("192.168.1.1", 5432)
# If another script tries to alter the port, Python throws a FrozenInstanceError
prod_db.port = 9090