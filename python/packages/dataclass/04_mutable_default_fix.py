# Never use an empty list [] or dictionary {} as a default value in a class,
# because all instances will share that exact same list in memory.
# Dataclasses fix this using the field function and a default_factory. 
# This is crucial when an AI model has a list of layers, or a server has a list of open ports.

from dataclasses import dataclass, field

@dataclass 
class DockerContainer:
    name: str
    # Every new container gets its own fresh, isolated empty list
    open_ports: list[int] = field(default_factory=list)

web = DockerContainer("nginx")
web.open_ports.append(80) 
# web.open_ports is now [80]
db = DockerContainer("postgress")
# db.open_ports is still []

