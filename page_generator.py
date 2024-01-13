import os
from pathlib import Path

# 1. 遍历chxx文件夹生成index.html
index_page_content = ''

p = Path('.')
for f in sorted(list(p.glob('ch*'))):
    if f.is_dir():
        index_page_content += f'<a href="{f.name}.html">{f.name}</a><br>\n'

        chapter_page_content = '<head>\n'
        chapter_page_content += '\t<link rel="stylesheet" href="main.css" />\n'
        chapter_page_content += '</head>\n'
        chapter_page_content += f'<h1>{f.name.replace("_", " ")}</h1>\n'
        chapter_page_content += '<a id="back" href="index.html">BACK</a>\n'
        chapter_page_content += '<div id="imgs">\n'
        # 2. 遍历chxx文件夹，生成每一章的html文件
        for image_name in sorted(os.listdir(f.name)):
            chapter_page_content += f'\t<img src="{f.name}/{image_name}">\n'
        chapter_page_content += '</div>\n'

        with open(f'{f.name}.html', 'w') as chapter_page:
            chapter_page.write(chapter_page_content)

with open('index.html', 'w') as index_page:
    index_page.write(index_page_content)
