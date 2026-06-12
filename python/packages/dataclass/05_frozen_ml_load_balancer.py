from dataclasses import dataclass, field

@dataclass(frozen=True)
class InterferenceServer:
    ip_address: str
    max_requests: int
    active_models: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.max_requests > 10000:
            raise ValueError("Max requests cannot exceed 10,000 to prevent server crashes.")
        


node_one = InterferenceServer("192.168.1.1", 3000)

# node_one.ip_address = "10.0.0.1"

node_two = InterferenceServer("192.168.1.0", 500000)