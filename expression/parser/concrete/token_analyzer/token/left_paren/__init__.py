from expression.parser.concrete.token_analyzer.token import Token, TokenType


class LeftParenToken (Token):
  def get_type (self) -> TokenType.LEFT_PAREN:
    return TokenType.LEFT_PAREN

  def get_value (self) -> str:
    return "("
