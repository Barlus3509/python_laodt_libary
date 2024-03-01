from python_laodt import *

data = '''ນີ້ຄືຕົວຢ່າງ python laodt libary ໝາກກ້ຽງ ຄວາຍ ໂປແກມເມີອາຍຸນ້ອຍ'''

en_text = lao_dte(data)

print(f'Text to array :  {en_text}')

de_text = lao_dtd(en_text)

print(f'Array to text :  {de_text}')