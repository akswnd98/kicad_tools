from expression.parser.expression.attribute import Attribute


class QuotedAttribute (Attribute):
  def __init__ (self, body: str):
    self.set_body(body)

  def set_body (self, body: str) -> None:
    self._body = body

  def get_value (self) -> str:
    return f"\"{self._body}\""
