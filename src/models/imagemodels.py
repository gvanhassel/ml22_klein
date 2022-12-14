import gin
import torch
from torch import nn


@gin.configurable
class CNN(nn.Module):
    def __init__(
        self, num_classes: int, kernel_size: int, filter1: int, filter2: int, unit1: int, unit2: int
    ) -> None:
        super().__init__()

        self.convolutions = nn.Sequential(
            nn.Conv2d(1, filter1, kernel_size=kernel_size, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(filter1, filter2, kernel_size=kernel_size, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(filter2, 32, kernel_size=kernel_size, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )

        self.dense = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128, unit1),
            nn.ReLU(),
            nn.Linear(unit1, unit2),
            nn.ReLU(),
            nn.Linear(unit2, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.convolutions(x)
        logits = self.dense(x)
        return logits

@gin.configurable
class CNN_150(nn.Module):
    def __init__(
        self, num_classes: int, kernel_size: int, filter1: int, filter2: int, unit1: int, unit2: int
    ) -> None:
        super().__init__()

        self.convolutions = nn.Sequential(
            nn.Conv2d(1, filter1, kernel_size=2, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(filter1, filter1, kernel_size=2, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(filter1, filter2, kernel_size=2, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(filter2, 32, kernel_size=2, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )

        self.dense = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128, unit1),
            nn.ReLU(),
            nn.Linear(unit1, unit1),
            nn.ReLU(),
            nn.Linear(unit1, unit2),
            nn.ReLU(),
            nn.Linear(unit2, unit2),
            nn.ReLU(),
            nn.Linear(unit2, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.convolutions(x)
        logits = self.dense(x)
        return logits
