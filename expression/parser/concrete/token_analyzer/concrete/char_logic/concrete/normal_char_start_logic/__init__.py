from expression.parser.concrete.token_analyzer.concrete.char_logic import IndividualCharLogic, Report
from expression.parser.concrete.token_analyzer.concrete.char_logic.report.concrete import ConcreteReport
from expression.parser.concrete.token_analyzer.token.normal_attribute import NormalAttributeToken
from utils.char_classifier.normal import Normal
from utils.char_classifier.right_paren import RightParen
from utils.char_classifier.whitespace import Whitespace


class NormalCharStartLogic (IndividualCharLogic):
  def __init__ (self):
    super().__init__(Normal())

  def process_main_logic (self, source: str, idx: int) -> Report:
    i = idx
    while i < len(source) and Normal().check(source[i]):
      i += 1
    
    if not Whitespace().check(source[i]) and not RightParen().check(source[i]):
      raise ValueError("White space or right parenthesis is expected after normal string")
    
    return ConcreteReport([NormalAttributeToken(source[idx: i])], i - idx)
