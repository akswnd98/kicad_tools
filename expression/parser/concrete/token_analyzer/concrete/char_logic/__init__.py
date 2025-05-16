from abc import ABC, abstractmethod
from typing import List

from expression.parser.concrete.token_analyzer.token import Token
from utils.char_classifier import CharClassifier

class Report (ABC):
  @abstractmethod
  def get_tokens (self) -> List[Token]:
    pass
  
  @abstractmethod
  def get_processed_char_num (self) -> int:
    pass

class CharLogic (ABC):
  @abstractmethod
  def process (self, source: str, idx: int) -> Report:
    pass

class IndividualCharLogic (CharLogic):
  _char_classifier: CharClassifier

  def __init__ (self, char_classifier: CharClassifier):
    self._char_classifier = char_classifier

  def process (self, source: str, idx: int) -> Report:
    if self._char_classifier.check(source[idx]):
      return self.process_main_logic(source, idx)
    else:
      raise ValueError("Char classifier not matched")

  @abstractmethod
  def process_main_logic (self, source: str, idx: int) -> Report:
    pass
