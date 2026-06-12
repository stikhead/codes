from dataclasses import dataclass

@dataclass
class TrainingConfig:
    model_name: str
    batch_size: int
    # this runs right after hidden __init__ finishes
    def __post_init__(self):
        if self.batch_size <= 0:
            raise ValueError(f"fatal error: batch size must be > 0. got {self.batch_size}")
        

# immediately crash and protects the pipeline
for i in range(5)[::-1]:
    
    print(TrainingConfig("resnet", i))