from typing import Callable
from expression.parser.concrete.token_analyzer.token import Token, TokenType
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state import State


class ExpressionOpenningState (State):
  def process_step (self, token: Token, context: Context, change_state: Callable[[State], None]) -> None:
    if token.get_type() == TokenType.TOKEN:
      context.enter_to_new_expression(token.get_value())
      from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.expression_opened import ExpressionOpenedState
      change_state(ExpressionOpenedState())
    else:
      raise Exception(f"ExpressionOpenningState failed: Unexpected token type: {token.get_type().value}\nExpected: {TokenType.TOKEN.value}")
