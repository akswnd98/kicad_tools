from typing import Callable
from expression.parser.concrete.token_analyzer.token import Token
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state import State

class ClosedState (State):
  def process_step (self, token: Token, context: Context, change_state: Callable[[State], None]) -> None:
    raise Exception("ClosedState failed: ExpressionBuilder is closed")
