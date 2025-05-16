from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack (Generic[T]):
  _data: List[T]

  def __init__ (self):
    self._data = []

  def push (self, item: T):
    self._data.append(item)

  def top (self) -> T:
    if self.check_empty():
      raise Exception("Stack is empty")

    return self._data[-1]

  def pop (self) -> None:
    if self.check_empty():
      raise Exception("Stack is empty")

    self._data.pop()

  def size (self) -> int:
    return len(self._data)

  def check_empty (self) -> bool:
    return len(self._data) <= 0
