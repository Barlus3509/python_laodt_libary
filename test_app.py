from python_laodt import *

data = '''ຂ້ອຍບາລັດຄູດາ ຄວາມໝາຍ ທົດລອງ ທົດສອບ ສ້າງງມັນ'''

en_text = lao_dte(data)

print(f'Text to array :  {en_text}')

de_text = lao_dtd(en_text)

print(f'Array to text :  {de_text}')