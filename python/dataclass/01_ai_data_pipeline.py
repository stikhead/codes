from dataclasses import dataclass

@dataclass
class TrainingConfig:
    model_name: str
    batch_size: int
    learning_rate: float


config = TrainingConfig("ResNet50", 32, 0.001)
print(config)