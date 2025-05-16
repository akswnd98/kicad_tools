from expression.parser.concrete import ConcreteParser

# python -m expression.parser.test3
if __name__ == '__main__':
  parser = ConcreteParser()
  source = "(symbol value)"
  result_expr = parser.parse(source)
  print(result_expr.convert_to_dict())
