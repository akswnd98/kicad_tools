from expression.parser.concrete.token_analyzer.concrete.char_logic import IndividualCharLogic, Report
from expression.parser.concrete.token_analyzer.concrete.char_logic.report.concrete import ConcreteReport
from utils.char_classifier.whitespace import Whitespace


class WhitespaceStartLogic (IndividualCharLogic):
  def __init__ (self):
    super().__init__(Whitespace())

  def process_main_logic (self, source: str, idx: int) -> Report:
    return ConcreteReport([], 1)
