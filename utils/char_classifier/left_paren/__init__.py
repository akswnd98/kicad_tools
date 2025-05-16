from utils.char_classifier import CharClassifier


class LeftParen (CharClassifier):
  def check (self, char: str) -> bool:
    return char == '('
