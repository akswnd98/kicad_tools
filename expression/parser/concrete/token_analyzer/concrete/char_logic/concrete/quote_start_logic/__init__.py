from expression.parser.concrete.token_analyzer.concrete.char_logic import IndividualCharLogic, Report
from expression.parser.concrete.token_analyzer.concrete.char_logic.report.concrete import ConcreteReport
from expression.parser.concrete.token_analyzer.token.quoted_attribute import QuotedAttributeToken
from utils.char_classifier.quote import Quote


class QuoteStartLogic (IndividualCharLogic):
  def __init__ (self):
    super().__init__(Quote())

  def process_main_logic (self, source: str, idx: int) -> Report:
    i = idx + 1
    while i < len(source) and source[i] != '"':
      i += 1
    
    if i >= len(source):
      raise ValueError("Quote is not closed")
    
    i += 1

    return ConcreteReport([QuotedAttributeToken(source[idx + 1: i - 1])], i - idx)
