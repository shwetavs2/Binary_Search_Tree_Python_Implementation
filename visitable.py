from abc import ABC, abstractmethod

class Visitable(ABC):
    """
    The Visitable interface declares an `accept` method that should take the
    base visitor interface as an argument.
    """

    @abstractmethod
    def accept(self, visitor) -> None:
        pass