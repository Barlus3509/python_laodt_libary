from python_laodt import *

data = '''ຂໍ້ຄວາມ'''

en_text = lao_dte(data)     #ການແຍກຂໍ້ຄວາມໄປເປັນ Array
print(f'Text to array :  {en_text}')

de_text = lao_dtd(en_text)      #ການເອົາ Array ກັບໄປເປັນຂໍ້ຄວາມ
print(f'Array to text :  {de_text}')