from expression.parser import Expression, Parser
from expression.parser.concrete.token_analyzer import TokenAnalyzer
from expression.parser.concrete.token_analyzer.concrete import ConcreteTokenAnalyzer
from expression.parser.concrete.token_tape_interpreter import TokenTapeInterpreter
from expression.parser.concrete.token_tape_interpreter.concrete import ConcreteTokenTapeInterpreter

class ConcreteParser (Parser):
  _token_analyzer: TokenAnalyzer
  _token_tape_interpreter: TokenTapeInterpreter

  def __init__ (self):
    self._token_analyzer = ConcreteTokenAnalyzer()
    self._token_tape_interpreter = ConcreteTokenTapeInterpreter()

  def parse (self, source: str) -> Expression:
    tokens = self._token_analyzer.analyze(source)
    return self._token_tape_interpreter.interpret(tokens)
