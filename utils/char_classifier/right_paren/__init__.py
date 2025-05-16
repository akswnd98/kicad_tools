from utils.char_classifier import CharClassifier


class RightParen (CharClassifier):
  def check (self, char: str) -> bool:
    return char == ')'
