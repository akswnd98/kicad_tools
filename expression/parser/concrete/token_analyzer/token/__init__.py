from abc import ABC, abstractmethod
from enum import Enum


class TokenType (Enum):
  LEFT_PAREN = "LEFT_PAREN"
  RIGHT_PAREN = "RIGHT_PAREN"
  NORMAL_ATTRIBUTE = "NORMAL_ATTRIBUTE"
  QUOTED_ATTRIBUTE = "QUOTED_ATTRIBUTE"
  TOKEN = "TOKEN"

class Token (ABC):
  @abstractmethod
  def get_type (self) -> TokenType:
    pass
  
  @abstractmethod
  def get_value (self) -> str:
    pass
