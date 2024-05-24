def remove_before_symbol(text, symbol):
    before, sep, after = text.partition(symbol)

# 示例字符串
text = "Hello, world! How are you?"

# 要删除的符号之前的内容
symbol = '!'

print(before)
