from typing import List
from expression.parser.concrete.token_tape_interpreter import TokenTapeInterpreter
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder import ExpressionBuilder
from expression.parser.concrete.token_tape_interpreter.concrete.expression_builder.concrete import ConcreteExpressionBuilder
from expression.parser.expression import Expression
from expression.parser.concrete.token_analyzer.token import Token

class ConcreteTokenTapeInterpreter (TokenTapeInterpreter):
  def interpret (self, tokens: List[Token]) -> Expression:
    expression_builder = ConcreteExpressionBuilder()
    for i, token in enumerate(tokens):
      try:
        expression_builder.process_step(token)
      except Exception as e:
        raise Exception(f"ConcreteTokenTapeInterpreter failed: tokens: {[(token.get_type().value, token.get_value()) for token in tokens]} Error at token {i}: {e}")

    return expression_builder.get_expression()
