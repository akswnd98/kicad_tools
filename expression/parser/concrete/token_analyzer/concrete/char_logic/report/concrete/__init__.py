from expression.parser.concrete.token_analyzer.concrete.char_logic import Report
from expression.parser.concrete.token_analyzer.token import Token
from typing import List

class ConcreteReport (Report):
  _tokens: List[Token]
  _processed_char_num: int

  def __init__ (self, tokens: List[Token], processed_char_num: int):
    self._tokens = tokens
    self._processed_char_num = processed_char_num

  def get_tokens (self) -> List[Token]:
    return self._tokens

  def get_processed_char_num (self) -> int:
    return self._processed_char_num
