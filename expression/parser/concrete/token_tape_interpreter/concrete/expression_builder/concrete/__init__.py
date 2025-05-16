from expression.parser.concrete.token_analyzer.token import Token
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder import ExpressionBuilder
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context.concrete import ConcreteContext
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state import State
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.state.concrete.initial import InitialState
from expression.parser.expression import Expression
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete.context import Context


class ConcreteExpressionBuilder (ExpressionBuilder):
  _state: State
  _context: Context

  def __init__ (self):
    self._state = InitialState()
    self._context = ConcreteContext()

  def process_step (self, token: Token) -> None:
    self._state.process_step(token, self._context, lambda state: self._change_state(state))

  def get_expression (self) -> Expression:
    return self._context.get_expression()

  def _change_state (self, state: State) -> None:
    self._state = state
