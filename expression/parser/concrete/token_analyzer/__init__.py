from abc import ABCMeta, abstractmethod
from typing import List

from expression.parser.concrete.token_analyzer.token import Token


class TokenAnalyzer (metaclass = ABCMeta):
  @abstractmethod
  def analyze (self, source: str) -> List[Token]:
    pass
