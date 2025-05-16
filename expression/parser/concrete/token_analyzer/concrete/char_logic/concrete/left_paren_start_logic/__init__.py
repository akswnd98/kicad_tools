from expression.parser.concrete.token_analyzer.concrete.char_logic import IndividualCharLogic, Report

from expression.parser.concrete.token_analyzer.concrete.char_logic.report.concrete import ConcreteReport
from expression.parser.concrete.token_analyzer.token.left_paren import LeftParenToken
from expression.parser.concrete.token_analyzer.token.token import TokenToken
from utils.char_classifier.left_paren import LeftParen
from utils.char_classifier.normal import Normal


class LeftParenStartLogic (IndividualCharLogic):
  def __init__ (self):
    super().__init__(LeftParen())

  def process_main_logic (self, source: str, idx: int) -> Report:
    i = idx + 1
    while i < len(source) and Normal().check(source[i]):
      i += 1
    
    return ConcreteReport(
      [LeftParenToken()]
      + [TokenToken(source[idx + 1: i])] if i > idx + 1 else [],
      i - idx
    )
