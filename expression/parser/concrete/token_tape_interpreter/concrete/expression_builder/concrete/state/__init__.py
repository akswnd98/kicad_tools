from abc import ABC, abstractmethod
from typing import Callable
from expression.parser.concrete.token_analyzer.token import Token
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context

class State (ABC):
  @abstractmethod
  def process_step (self, token: Token, context: Context, change_state: Callable[["State"], None]) -> None:
    pass
