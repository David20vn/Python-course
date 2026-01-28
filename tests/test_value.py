from own_librarie import hello

def test_value_hello ():
  assert hello("David") == "Hello, David"
  assert hello("Santiago") == "Hello, Santiago"