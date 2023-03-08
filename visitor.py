from abc import ABC, abstractmethod
class Visitor(ABC):
    """Visitor interface that takes abstarct methods for the Visitor classes implementation"""
    @abstractmethod
    def longest_path(self, element) -> None:
        pass

    @abstractmethod
    def average_path(self, element) -> None:
        pass

    @abstractmethod
    def leaf_count(self, element) -> None:
        pass

    @abstractmethod
    def single_node_count(self, element) -> None:
        pass