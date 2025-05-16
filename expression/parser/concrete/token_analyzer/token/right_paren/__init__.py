from expression.parser.concrete.token_analyzer.token import Token, TokenType


class RightParenToken (Token):
  def get_type (self) -> TokenType.RIGHT_PAREN:
    return TokenType.RIGHT_PAREN

  def get_value (self) -> str:
    return ")"
