from typing import List
from expression.parser.expression import Attribute, Expression

class ConcreteExpression (Expression):
  _token: str
  _expressions: List[Expression]
  _attributes: List[Attribute]

  def __init__ (self, token: str, expressions: List[Expression], attributes: List[Attribute]):
    self._token = token
    self._expressions = expressions
    self._attributes = attributes
  
  @property
  def token (self) -> str:
    return self._token

  @property
  def expressions (self) -> List[Expression]:
    return self._expressions

  @property
  def attributes (self) -> List[Attribute]:
    return self._attributes

  def convert_to_dict (self) -> dict:
    return {
      "token": self._token,
      "expressions": [expression.convert_to_dict() for expression in self._expressions],
      "attributes": [attribute.get_value() for attribute in self._attributes]
    }
