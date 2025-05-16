from abc import ABCMeta, abstractmethod

from expression.parser.expression import Expression

class Parser (metaclass = ABCMeta):
  @abstractmethod
  def parse (self, source: str) -> Expression:
    pass
