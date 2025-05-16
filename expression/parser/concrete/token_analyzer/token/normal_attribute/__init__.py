from expression.parser.concrete.token_analyzer.token import Token, TokenType


class NormalAttributeToken (Token):
  _value: str

  def __init__ (self, value: str):
    self._value = value

  def get_type (self) -> TokenType.NORMAL_ATTRIBUTE:
    return TokenType.NORMAL_ATTRIBUTE

  def get_value (self) -> str:
    return self._value
