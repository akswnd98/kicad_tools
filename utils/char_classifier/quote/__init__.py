from utils.char_classifier import CharClassifier


class Quote (CharClassifier):
  def check (self, char: str) -> bool:
    return char == '"'
