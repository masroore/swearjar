import glob
from os import path
import json
import codecs

tmp_list = []

for f in glob.glob(path.abspath('./list/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        list = json.loads(fp.read())
        tmp_list.extend([x.strip().lower() for x in list if x.strip()])

for f in glob.glob(path.abspath('./langs/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        list = json.loads(fp.read())
        tmp_list.extend([x.strip().lower() for x in list if x.strip()])

for f in glob.glob(path.abspath('./dict/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        dict = json.loads(fp.read())
        tmp_list.extend([x.strip().lower() for x in dict.keys() if x.strip()])

for f in glob.glob(path.abspath('./txt/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        line = fp.read()
        tmp_list.extend([x.strip().lower() for x in line.split(',') if x.strip()])

tmp_list= [x.strip(' \n\r*-,;!') for x in tmp_list]
tmp_list= [x.replace('@', 'a').replace('*', '-') for x in tmp_list]
tmp_list = set(tmp_list)


final = []
for t in tmp_list:
    t = t.replace(' ', '-')
    final.append(t)
    if '-' in t:
        final.append(t.replace('-', ''))

final = sorted(set(final))
with codecs.open('badwords.json', 'w', encoding='utf8') as fp:
    #fp.write('\n'.join(final))
    fp.write(json.dumps(final, indent=1, ensure_ascii=False))
