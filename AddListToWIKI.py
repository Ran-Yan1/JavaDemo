#! python3
"""从剪贴板中取得文本，在每一行开始处加上星号和空
格，然后将这段新的文本贴回到剪贴板
"""
from posixpath import split
import pyperclip
txt=pyperclip.paste()
lines=txt.split('\n')#用/n将txt分成字符串列表
for i in range(len(lines)):
    lines[i]='* '+lines[i]
txt='\n'.join(lines)
print(txt)
pyperclip.copy(txt)
