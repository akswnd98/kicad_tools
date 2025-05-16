from utils.char_classifier import CharClassifier


class Whitespace (CharClassifier):
  def check (self, char: str) -> bool:
    return char.isspace()
