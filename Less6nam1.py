"Hello Volodymyr "


import os 
import shutil

extensions = {
    'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
    'videos': ['AVI', 'MP4', 'MOV', 'MKV'],
    'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'music': ['MP3', 'OGG', 'WAV', 'AMR'],
    'archives': ['ZIP', 'GZ', 'TAR']
}

def normalize(name):
    translit = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 
        'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
    }

text = " "
lines = text.split()
max_len = max(len(word) for word in lines)
result = []
for word in lines:
    result.append(word + " "*(max_len - len(word)))
output = "\n".join(result)
print(output)
