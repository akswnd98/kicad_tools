from abc import ABC, abstractmethod
from expression.parser.expression import Attribute, Expression

class Context (ABC):
  @abstractmethod
  def get_expression (self) -> Expression:
    pass

  @abstractmethod
  def add_attribute (self, attribute: Attribute) -> None:
    pass

  @abstractmethod
  def check_closed (self) -> bool:
    pass

  @abstractmethod
  def enter_to_new_expression (self, token: str) -> None:
    pass

  @abstractmethod
  def leave_current_expression (self) -> None:
    pass
