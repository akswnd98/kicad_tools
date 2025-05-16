from abc import ABC, ABCMeta, abstractmethod
from typing import List

from expression.parser import Expression
from expression.parser.concrete.token_analyzer.token import Token

class TokenTapeInterpreter (metaclass = ABCMeta):
  @abstractmethod
  def interpret (self, tokens: List[Token]) -> Expression:
    pass
