import unittest
from expression.parser.concrete import ConcreteParser
# We rely on the Expression object's convert_to_dict() method for assertions,
# as the concrete Expression and Attribute classes are not directly tested here.

class TestConcreteParser(unittest.TestCase):
  def setUp(self):
    self.parser = ConcreteParser()

  def test_simple_expression(self):
    """Tests parsing a simple S-expression: (token child_token)"""
    source = "(symbol value)"
    expected_dict = {
      'token': 'symbol',
      'expression': [],
      'attributes': ['value']
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_nested_expression(self):
    """Tests parsing a nested S-expression: (token (child_token (grandchild_token)))"""
    source = "(outer (inner value))"
    expected_dict = {
      'token': 'outer',
      'expressions': [
        {
          'token': 'inner',
          'expressions': [
            {'token': 'value', 'expressions': [], 'attributes': []}
          ],
          'attributes': []
        }
      ],
      'attributes': []
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_multiple_elements_at_same_level(self):
    """Tests parsing an S-expression with multiple child tokens: (token child1 child2 child3)"""
    source = "(node item1 item2 item3)"
    expected_dict = {
      'token': 'node',
      'expressions': [
        {'token': 'item1', 'expressions': [], 'attributes': []},
        {'token': 'item2', 'expressions': [], 'attributes': []},
        {'token': 'item3', 'expressions': [], 'attributes': []}
      ],
      'attributes': []
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_expression_with_only_token(self):
    """Tests parsing an S-expression with no children: (token)"""
    source = "(token_only)"
    expected_dict = {'token': 'token_only', 'expressions': [], 'attributes': []}
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_expression_with_quoted_strings_and_numbers(self):
    """Tests parsing S-expressions with quoted strings and numeric literals.
    Assumes strings are unquoted by the tokenizer/parser.
    """
    source = '(data "hello world" 123 "another item")'
    expected_dict = {
      'token': 'data',
      'expressions': [
        {'token': 'hello world', 'expressions': [], 'attributes': []},
        {'token': '123', 'expressions': [], 'attributes': []},
        {'token': 'another item', 'expressions': [], 'attributes': []}
      ],
      'attributes': []
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_kicad_style_property_as_regular_expression(self):
    """Tests if a Kicad-style property (e.g., (property "Key" "Value"))
    is parsed as a standard nested expression.
    """
    source = '(property "Key" "Value")'
    expected_dict = {
      'token': 'property',
      'expressions': [
        {'token': 'Key', 'expressions': [], 'attributes': []},
        {'token': 'Value', 'expressions': [], 'attributes': []}
      ],
      'attributes': []
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_simple_multiline_expression(self):
    """Tests parsing a simple S-expression formatted with newlines and tabs."""
    source = """(
      symbol
        value
    )"""
    expected_dict = {
      'token': 'symbol',
      'expressions': [{'token': 'value', 'expressions': [], 'attributes': []}],
      'attributes': []
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_nested_multiline_expression(self):
    """Tests parsing a nested S-expression formatted with newlines and tabs."""
    source = """(
      outer
      (
        inner
        value
      )
    )"""
    expected_dict = {
      'token': 'outer',
      'expressions': [
        {
          'token': 'inner',
          'expressions': [
            {'token': 'value', 'expressions': [], 'attributes': []}
          ],
          'attributes': []
        }
      ],
      'attributes': []
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  def test_multiple_elements_multiline_expression(self):
    """Tests parsing an S-expression with multiple elements, formatted with newlines and tabs."""
    source = """(
      node
      item1
      item2
      item3
    )"""
    expected_dict = {
      'token': 'node',
      'expressions': [
        {'token': 'item1', 'expressions': [], 'attributes': []},
        {'token': 'item2', 'expressions': [], 'attributes': []},
        {'token': 'item3', 'expressions': [], 'attributes': []}
      ],
      'attributes': []
    }
    result_expr = self.parser.parse(source)
    self.assertEqual(result_expr.convert_to_dict(), expected_dict)

  # Future test considerations:
  # - Malformed S-expressions (e.g., unbalanced parentheses, unexpected characters)
  #   and how the parser handles errors (e.g., raises specific exceptions).
  # - S-expressions that should result in populated 'attributes' list,
  #   once the logic for attribute identification by the parser and the
  #   structure of Attribute.convert_to_dict() (or similar representation) is clarified.
  # - Empty input string or input with only whitespace.
  # - Input like "()" (empty S-expression) if it's a valid case.

# python -m unittest expression.parser.test
if __name__ == '__main__':
  unittest.main()
