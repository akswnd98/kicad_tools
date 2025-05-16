from utils.char_classifier import CharClassifier


class Alphabet (CharClassifier):
  def check (self, char: str) -> bool:
    return char.isalpha()
