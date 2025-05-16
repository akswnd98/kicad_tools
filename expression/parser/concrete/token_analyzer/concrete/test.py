from expression.parser.concrete.token_analyzer.concrete import ConcreteTokenAnalyzer

# python -m expression.parser.concrete.token_analyzer.concrete.test
if __name__ == "__main__":
  token_analyzer = ConcreteTokenAnalyzer()
  tokens = token_analyzer.analyze("(hello (world))")
  tokens = token_analyzer.analyze("(hello sasdf)")
  tokens = token_analyzer.analyze("(symbol (nested_symbol value1) (another_nested value2))")

  print([(token.get_value(), token.get_type().value) for token in tokens])
