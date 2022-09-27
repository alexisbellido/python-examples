if __name__ == "__main__":

  # https://docs.python.org/3/reference/lexical_analysis.html#integers

  print('converting decimal, binary and hexadecimal numbers')

  num_decimal = 27
  num_binary = bin(num_decimal)
  num_octal = oct(num_decimal)
  num_hex = hex(num_decimal)

  print('num_decimal', num_decimal)
  print('num_binary', num_binary, 'num_decimal', int(num_binary, 2))
  print('num_octal', num_octal, 'num_decimal', int(num_octal, 8))
  print('num_hex', num_hex, 'num_decimal', int(num_hex, 16))

  # num_literal_binary = '111'
  num_literal_binary = '0b111'
  print(int(num_literal_binary, 2))

  num_literal_octal = '0o3456'
  print(int(num_literal_octal, 8))

  num_literal_hex = '0x24bb44'
  print(int(num_literal_hex, 16))
