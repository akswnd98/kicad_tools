from typing import Callable
from expression.parser.concrete.token_analyzer.token import Token, TokenType
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state import State

class AttributeEndedState (State):
  def process_step (self, token: Token, context: Context, change_state: Callable[[State], None]) -> None:
    if token.get_type() == TokenType.LEFT_PAREN:
      from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.expression_openning import ExpressionOpenningState
      change_state(ExpressionOpenningState())
    elif token.get_type() == TokenType.RIGHT_PAREN:
      self._process_right_paren_follow(context, change_state)
    else:
      raise Exception(f"AttributeEndedState failed: Unexpected token type: {token.get_type().value}\nExpected: {TokenType.LEFT_PAREN.value} or {TokenType.RIGHT_PAREN.value}")

  def _process_right_paren_follow (self, context: Context, change_state: Callable[[State], None]) -> None:
    context.leave_current_expression()
    if context.check_closed():
      from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.closed import ClosedState
      change_state(ClosedState())
    else:
      from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.attribute_ended import AttributeEndedState
      change_state(AttributeEndedState())
