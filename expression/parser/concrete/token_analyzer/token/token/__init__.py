from expression.parser.concrete.token_analyzer.token import Token, TokenType


class TokenToken (Token):
  _value: str

  def __init__ (self, value: str):
    self._value = value

  def get_type (self) -> TokenType.TOKEN:
    return TokenType.TOKEN

  def get_value (self) -> str:
    return self._value
