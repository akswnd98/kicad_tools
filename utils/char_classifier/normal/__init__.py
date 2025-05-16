from utils.char_classifier import CharClassifier


class Normal (CharClassifier):
  def check (self, char: str) -> bool:
    return char.isalnum() or char in "._-:"
