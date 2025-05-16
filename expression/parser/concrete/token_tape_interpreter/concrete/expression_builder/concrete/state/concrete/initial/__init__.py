from typing import Callable
from expression.parser.concrete.token_analyzer.token import Token, TokenType
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state import State


class InitialState (State):
  def process_step (self, token: Token, context: Context, change_state: Callable[[State], None]) -> None:
    if token.get_type() == TokenType.LEFT_PAREN:
      from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.expression_openning import ExpressionOpenningState
      change_state(ExpressionOpenningState())
    else:
      raise Exception(f"InitialState failed: Unexpected token type: {token.get_type().value}\nExpected: {TokenType.LEFT_PAREN.value}")
