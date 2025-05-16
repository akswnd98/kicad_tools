from abc import ABC, abstractmethod
from typing import List

from expression.parser.expression.attribute import Attribute

class Expression (ABC):
  @property
  @abstractmethod
  def token (self) -> str:
    pass

  @property
  @abstractmethod
  def expressions (self) -> List["Expression"]:
    pass

  @property
  @abstractmethod
  def attributes (self) -> List[Attribute]:
    pass

  @abstractmethod
  def convert_to_dict (self) -> dict:
    pass
