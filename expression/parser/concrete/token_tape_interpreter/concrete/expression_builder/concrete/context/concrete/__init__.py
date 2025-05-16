from typing import Optional
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context
from expression.parser.expression import Attribute, Expression
from expression.parser.expression.concrete import ConcreteExpression
from utils.stack import Stack

class ConcreteContext (Context):
  _current_expression: Optional[Expression]
  _stack: Stack[Expression]

  def __init__ (self):
    self._stack = Stack()

  def get_expression (self) -> Expression:
    if self._current_expression is None:
      raise Exception("context is in initial state")
    return self._current_expression

  def add_attribute (self, attribute: Attribute) -> None:
    self._stack.top().attributes.append(attribute)

  def check_closed (self) -> bool:
    return self._current_expression is not None and self._stack.check_empty()

  def enter_to_new_expression (self, token: str) -> None:
    self._stack.push(ConcreteExpression(token, [], []))
    if self._stack.size() == 1:
      self._current_expression = self._stack.top()
  
  def leave_current_expression (self) -> None:
    closed_expression = self._stack.top()
    self._stack.pop()
    if not self._stack.check_empty():
      self._stack.top().expressions.append(closed_expression)

  def initialize (self) -> None:
    self._current_expression = None
    self._stack = Stack()
