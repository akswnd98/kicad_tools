from typing import List
from expression.parser.concrete.token_analyzer import TokenAnalyzer
from expression.parser.concrete.token_analyzer.concrete.char_logic.concrete import ConcreteCharLogic
from expression.parser.concrete.token_analyzer.token import Token

class ConcreteTokenAnalyzer (TokenAnalyzer):
  def analyze (self, source: str) -> List[Token]:
    char_logic = ConcreteCharLogic()
    i = 0
    ret = []
    while i < len(source):
      report = char_logic.process(source, i)
      i += report.get_processed_char_num()
      ret.extend(report.get_tokens())

    return ret
