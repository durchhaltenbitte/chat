#读取文档 计算每个人一共说了多少字

import os

def read(filename):
    content = []
    with open (filename, 'r') as f:
        for line in f:
            content.append(line.strip())
    return content

def compute(content):
    name = None
    allen = 0
    viki = 0  
    allen_stkr = 0
    viki_stkr = 0
    allen_img = 0
    viki_img = 0

    for lines in content:
        s = lines.split(' ')
        time = s[0]
        name = s[1]
        
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_stkr += 1
            elif s[2] == '圖片':
                allen_img += 1
            else:
                for words in s[2:]:
                    allen += len(words)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_stkr += 1
            elif s[2] == '圖片':
                viki_img += 1
            else:
                for words in s[2:]:
                    viki += len(words)

    print('Allen sent', allen, 'words', allen_stkr, 'stickers', 'and', allen_img, 'images.')
    print('Viki sent', viki, 'words', viki_stkr, 'stickers', 'and', viki_img, 'images.')

def main():
    filename = input('Please input text name:')
    if os.path.isfile(filename):
        print('Read succesfully!')
    content = read(filename)
    compute(content)

main()


    
