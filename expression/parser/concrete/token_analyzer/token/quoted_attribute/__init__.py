from expression.parser.concrete.token_analyzer.token import Token, TokenType


class QuotedAttributeToken (Token):
  _body: str

  def __init__ (self, body: str):
    self._body = body

  def get_type (self) -> TokenType.QUOTED_ATTRIBUTE:
    return TokenType.QUOTED_ATTRIBUTE

  def get_value (self) -> str:
    return self._body
