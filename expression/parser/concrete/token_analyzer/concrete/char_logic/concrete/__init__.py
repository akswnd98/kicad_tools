from typing import List
from expression.parser.concrete.token_analyzer.concrete.char_logic import CharLogic, Report
from expression.parser.concrete.token_analyzer.concrete.char_logic.concrete.left_paren_start_logic import LeftParenStartLogic
from expression.parser.concrete.token_analyzer.concrete.char_logic.concrete.normal_char_start_logic import NormalCharStartLogic
from expression.parser.concrete.token_analyzer.concrete.char_logic.concrete.quote_start_logic import QuoteStartLogic
from expression.parser.concrete.token_analyzer.concrete.char_logic.concrete.right_paren_start_logic import RightParenStartLogic
from expression.parser.concrete.token_analyzer.concrete.char_logic.concrete.whitespace_start_logic import WhitespaceStartLogic

class ConcreteCharLogic (CharLogic):
  _char_logics: List[CharLogic]

  def __init__ (self):
    self._char_logics = [
      LeftParenStartLogic(),
      RightParenStartLogic(),
      QuoteStartLogic(),
      NormalCharStartLogic(),
      WhitespaceStartLogic()
    ]

  def process (self, source: str, idx: int) -> Report:
    for char_logic in self._char_logics:
      try:
        return char_logic.process(source, idx)
      except ValueError:
        pass

    raise ValueError(f"No char logic found for character at index {idx} in source: {source}: ...{source[idx: idx + min(20, len(source) - idx)]}")
