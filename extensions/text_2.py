def remove_before_symbol(text, symbol):
    before, sep, after = text.partition(symbol)
    if sep:  # 检查分隔符是否存在
        return sep + after
    else:
        return text

# 示例字符串
text = "Hello, world! How are you?"

# 要删除的符号之前的内容
symbol = '!'

print(before)
