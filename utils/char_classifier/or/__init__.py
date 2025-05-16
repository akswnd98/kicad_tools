from typing import List

from utils.char_classifier import CharClassifier


class Or (CharClassifier):
  _classifiers: List[CharClassifier]

  def __init__ (self, classifiers: List[CharClassifier]):
    self._classifiers = classifiers

  def check (self, char: str) -> bool:
    for classifier in self._classifiers:
      if classifier.check(char):
        return True

    return False
