from abc import ABC, abstractmethod


class CharClassifier (ABC):
  @abstractmethod
  def check (self, char: str) -> bool:
    pass
