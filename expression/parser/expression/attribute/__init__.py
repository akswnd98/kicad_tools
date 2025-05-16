from abc import ABC, abstractmethod


class Attribute (ABC):
  @abstractmethod
  def set_body (self, body: str) -> None:
    pass

  @abstractmethod
  def get_value (self) -> str:
    pass
