from expression.parser.concrete.token_analyzer.concrete.char_logic import IndividualCharLogic, Report
from expression.parser.concrete.token_analyzer.concrete.char_logic.report.concrete import ConcreteReport
from expression.parser.concrete.token_analyzer.token.right_paren import RightParenToken
from utils.char_classifier.right_paren import RightParen


class RightParenStartLogic (IndividualCharLogic):
  def __init__ (self):
    super().__init__(RightParen())

  def process_main_logic (self, source: str, idx: int) -> Report:
    return ConcreteReport([RightParenToken()], 1)
