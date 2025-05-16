import json
from expression.parser.concrete import ConcreteParser


parser = ConcreteParser()

def test1 ():
  
  source = "(symbol value)"
  expected_dict = {
    'token': 'symbol',
    'expressions': [],
    'attributes': ['value']
  }
  result_expr = parser.parse(source)
  print("actual:", result_expr.convert_to_dict())
  print("expected:", expected_dict)
  assert result_expr.convert_to_dict() == expected_dict
  print("test1 passed")

def test2():
  source = "(symbol (nested_symbol value1) (another_nested value2))"
  expected_dict = {
    'token': 'symbol',
    'attributes': [],
    'expressions': [
      {'token': 'nested_symbol', 'attributes': ['value1'], 'expressions': []},
      {'token': 'another_nested', 'attributes': ['value2'], 'expressions': []}
    ]
  }
  result_expr = parser.parse(source)
  print("\nactual for test2:", result_expr.convert_to_dict())
  print("expected for test2:", expected_dict)
  assert result_expr.convert_to_dict() == expected_dict
  print("test2 passed")

def test3():
  source = '(symbol "quoted attribute" (nested_symbol "another quoted" 123) value)'
  try:
    parser.parse(source)
  except Exception as e:
    assert True
    print("test3 passed (assertion: parser handles malformed input strictly)")
    return
  
  print("test3 failed (assertion: parser should have raised an exception)")
  assert False

def test4():
  source = '(module version "1.0" author "AK" (export func1) (import libA))'
  expected_dict = {
    'token': 'module',
    'attributes': ['version', '"1.0"', 'author', '"AK"'],
    'expressions': [
      {'token': 'export', 'attributes': ['func1'], 'expressions': []},
      {'token': 'import', 'attributes': ['libA'], 'expressions': []}
    ]
  }
  result_expr = parser.parse(source)
  print("\nactual for test4:", result_expr.convert_to_dict())
  print("expected for test4:", expected_dict)
  assert result_expr.convert_to_dict() == expected_dict
  print("test4 passed")

def test5():
  source = '(component "Resistor" value 10k ref R1 (footprint "lib:0805") (datasheet "url"))'
  expected_dict = {
    'token': 'component',
    'attributes': ['"Resistor"', 'value', '10k', 'ref', 'R1'],
    'expressions': [
      {'token': 'footprint', 'attributes': ['"lib:0805"'], 'expressions': []},
      {'token': 'datasheet', 'attributes': ['"url"'], 'expressions': []}
    ]
  }
  result_expr = parser.parse(source)
  print("\nactual for test5:", result_expr.convert_to_dict())
  print("expected for test5:", expected_dict)
  assert result_expr.convert_to_dict() == expected_dict
  print("test5 passed")

def test6():
  source = '(level1 attr1 (level2 attr2 (level3 attr3 "val3")) (level2.1 attr2.1))'
  expected_dict = {
    'token': 'level1',
    'attributes': ['attr1'],
    'expressions': [
      {
        'token': 'level2',
        'attributes': ['attr2'],
        'expressions': [
          {'token': 'level3', 'attributes': ['attr3', '"val3"'], 'expressions': []}
        ]
      },
      {
        'token': 'level2.1',
        'attributes': ['attr2.1'],
        'expressions': []
      }
    ]
  }
  result_expr = parser.parse(source)
  print("\nactual for test6:", result_expr.convert_to_dict())
  print("expected for test6:", expected_dict)
  assert result_expr.convert_to_dict() == expected_dict
  print("test6 passed")

def test7():
  source = '''
    (module fancy_module
      (version "2.0")
      (description "A module with multi-line formatting.")
      (components
        (comp (ref U1) (value "MCU")
          (pins
            (pin 1 (type input) (name GPIO1))
            (pin 2 (type output) (name LED_CTRL))
          )
        )
      )
      (config
        (debug enabled)
        (priority high)
      )
    )
  '''
  expected_dict = {
    'token': 'module',
    'attributes': ['fancy_module'],
    'expressions': [
      {'token': 'version', 'attributes': ['"2.0"'], 'expressions': []},
      {'token': 'description', 'attributes': ['"A module with multi-line formatting."'], 'expressions': []},
      {
        'token': 'components',
        'attributes': [],
        'expressions': [
          {
            'token': 'comp',
            'attributes': ['(ref U1)', '(value "MCU")'], # Note: parser might treat these as single string attributes if not handling sub-attributes within them.
                                                      # This test assumes attributes are simple strings for now.
                                                      # If the parser is more sophisticated, this part needs adjustment.
            'expressions': [
              {
                'token': 'pins',
                'attributes': [],
                'expressions': [
                  {'token': 'pin', 'attributes': ['1', '(type input)', '(name GPIO1)'], 'expressions': []},
                  {'token': 'pin', 'attributes': ['2', '(type output)', '(name LED_CTRL)'], 'expressions': []}
                ]
              }
            ]
          }
        ]
      },
      {
        'token': 'config',
        'attributes': [],
        'expressions': [
          {'token': 'debug', 'attributes': ['enabled'], 'expressions': []},
          {'token': 'priority', 'attributes': ['high'], 'expressions': []}
        ]
      }
    ]
  }
  result_expr = parser.parse(source)
  print("\nactual for test7 (multi-line):", json.dumps(result_expr.convert_to_dict(), indent=2))
  print("\nexpected for test7 (multi-line):", json.dumps(expected_dict, indent=2))
  assert result_expr.convert_to_dict() == expected_dict
  print("test7 passed")

# python -m expression.parser.test2
if __name__ == '__main__':
  test1()
  test2()
  test3()
  test4()
  test5()
  test6()
  test7()
