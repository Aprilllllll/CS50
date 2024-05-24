def remove_before_symbol(text, symbol):
    parts = text.split(symbol, 1)
    if len(parts) > 1:
        return symbol + parts[1]
    else:
        return text

# 示例字符串
text = "Hello, world! How are you?"

# 要删除的符号之前的内容
symbol = '!'

# 调用函数并打印结果
result = remove_before_symbol(text, symbol)
print(result)
