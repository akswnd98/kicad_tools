from abc import ABC, abstractmethod
from typing import List

from expression.parser.concrete.token_analyzer.token import Token


class Report (ABC):
  @abstractmethod
  def get_tokens (self) -> List[Token]:
    pass
  
  @abstractmethod
  def get_processed_char_num (self) -> int:
    pass
