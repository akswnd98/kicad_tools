from abc import ABC, abstractmethod
from expression.parser.concrete.token_analyzer.token import Token
from expression.parser import Expression

class ExpressionBuilder (ABC):
  @abstractmethod
  def process_step (self, token: Token) -> None:
    pass

  @abstractmethod
  def get_expression (self) -> Expression:
    pass
