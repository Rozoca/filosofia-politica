from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from collections import Counter
import json,re,subprocess
ROOT=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self,t):super().__init__(convert_charrefs=True);self.ids=[];self.urls=[];self.h1=0;self.feed(t)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag in ['a','link','img','script','source','audio']:
   for key in ['href','src']:
    if key in a:self.urls.append(a[key])
pages={p.name:Page(p.read_text()) for p in ROOT.glob('*.html')};errors=[];incoming=Counter()
for name,p in pages.items():
 if p.h1!=1:errors.append(f'{name}: {p.h1} h1 headings')
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{name}: duplicate IDs')
 for u in p.urls:
  parts=urlsplit(u)
  if parts.scheme or parts.netloc:continue
  path=unquote(parts.path) or name
  if not (ROOT/path).exists():errors.append(f'{name}: missing {path}')
  elif path.endswith('.html'):
   incoming[path]+=1
   if parts.fragment and parts.fragment not in pages[path].ids:errors.append(f'{name}: missing anchor {u}')
for name in pages:
 if not incoming[name]:errors.append(f'orphan page: {name}')
mods=json.loads((ROOT/'data/modules.json').read_text());qs=json.loads((ROOT/'data/questions.json').read_text());cases=json.loads((ROOT/'data/cases.json').read_text());topics=json.loads((ROOT/'data/topics.json').read_text())
ids={m['id'] for m in mods};ts={t['title'] for t in topics}
assert len(qs)==40 and len({q['id'] for q in qs})==40
for q in qs:
 assert q['module'] in ids and len(q['options'])==4 and 0<=q['answer']<4
 assert q['level'] in [1,2,3,4] and q['difficulty'] in ['Básico','Intermedio','Avanzado']
 assert set(q['topics'])<=ts and len(q['explanation'])>100
assert all(sum(q['module']==m for q in qs)>=2 for m in ids)
assert sum(c['kind']=='caso' for c in cases)==8
for c in cases:assert set(c['modules'])<=ids
for p in ROOT.glob('*.html'):
 for i,s in enumerate(re.findall(r'<script>(.*?)</script>',p.read_text(),re.S)):
  check=subprocess.run(['node','--check'],input=s,text=True,capture_output=True)
  if check.returncode:errors.append(f'{p.name}: script {i}: {check.stderr}')
for p in (ROOT/'assets/js').glob('*.js'):
 check=subprocess.run(['node','--input-type=module','--check'],input=p.read_text(),text=True,capture_output=True)
 if check.returncode:errors.append(f'{p.name}: {check.stderr}')
print(json.dumps({'pages':len(pages),'modules':len(mods),'questions':len(qs),'caseFormats':dict(Counter(c['kind'] for c in cases)),'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
