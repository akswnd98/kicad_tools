from typing import List

from utils.char_classifier import CharClassifier


class And (CharClassifier):
  _classifiers: List[CharClassifier]

  def __init__ (self, classifiers: List[CharClassifier]):
    self._classifiers = classifiers

  def check (self, char: str) -> bool:
    for classifier in self._classifiers:
      if not classifier.check(char):
        return False

    return True
