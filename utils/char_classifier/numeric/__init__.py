from utils.char_classifier import CharClassifier


class Numeric (CharClassifier):
  def check (self, char: str) -> bool:
    return char.isdigit()
