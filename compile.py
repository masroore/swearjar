import glob
from os import path
import json
import codecs

words = []

for f in glob.glob(path.abspath('./list/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        list = json.loads(fp.read())
        words.extend([x.strip().lower() for x in list if x.strip()])

for f in glob.glob(path.abspath('./langs/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        list = json.loads(fp.read())
        words.extend([x.strip().lower() for x in list if x.strip()])

for f in glob.glob(path.abspath('./dict/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        dict = json.loads(fp.read())
        words.extend([x.strip().lower() for x in dict.keys() if x.strip()])

for f in glob.glob(path.abspath('./txt/*.*')):
    print(path.basename(f))
    with codecs.open(f, 'r', encoding='utf8') as fp:
        line = fp.read()
        words.extend([x.strip().lower() for x in line.split(',') if x.strip()])

words = [x.strip(' \n\r*-,;!') for x in words]
words = [x.replace('@', 'a').replace('*', '-') for x in words]
words = set(words)

final = []
for t in words:
    t = t.replace(' ', '-')
    final.append(t)
    if '-' in t:
        final.append(t.replace('-', ''))

final = sorted(set(final))
with codecs.open('swearjar.json', 'w', encoding='utf8') as fp:
    fp.write(json.dumps(final, indent=1, ensure_ascii=False))

with codecs.open('swearjar.txt', 'w', encoding='utf8') as fp:
    fp.write('\n'.join(final))