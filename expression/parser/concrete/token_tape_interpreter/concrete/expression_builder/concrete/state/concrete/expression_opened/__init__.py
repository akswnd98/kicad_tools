from typing import Callable
from expression.parser.concrete.token_analyzer.token import Token, TokenType
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state import State
from expression.parser.expression.attribute import Attribute
from expression.parser.expression.attribute.normal import NormalAttribute
from expression.parser.expression.attribute.quoted import QuotedAttribute


class ExpressionOpenedState (State):
  def process_step (self, token: Token, context: Context, change_state: Callable[[State], None]) -> None:
    if token.get_type() == TokenType.NORMAL_ATTRIBUTE:
      context.add_attribute(NormalAttribute(token.get_value()))
    elif token.get_type() == TokenType.QUOTED_ATTRIBUTE:
      context.add_attribute(QuotedAttribute(token.get_value()))
    elif token.get_type() == TokenType.LEFT_PAREN:
      self._process_left_paren_follow(change_state)
    elif token.get_type() == TokenType.RIGHT_PAREN:
      self._process_right_paren_follow(context, change_state)
    else:
      raise Exception(f"ExpressionOpenedState failed: Unexpected token type: {token.get_type().value}\nExpected: {TokenType.ATTRIBUTE.value} or {TokenType.LEFT_PAREN.value} or {TokenType.RIGHT_PAREN.value}")
  
  def _process_left_paren_follow (self, change_state: Callable[[State], None]) -> None:
    from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.expression_openning import ExpressionOpenningState
    change_state(ExpressionOpenningState())
  
  def _process_right_paren_follow (self, context: Context, change_state: Callable[[State], None]) -> None:
    context.leave_current_expression()
    if context.check_closed():
      from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.closed import ClosedState
      change_state(ClosedState())
    else:
      from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.attribute_ended import AttributeEndedState
      change_state(AttributeEndedState())
