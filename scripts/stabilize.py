"""One-time migration retained for audit; do not rerun on evolved pages."""
from pathlib import Path
import re,json,html
from html.parser import HTMLParser
class Ranges(HTMLParser):
 def __init__(self,text):
  super().__init__();self.text=text;self.offsets=[0];self.ranges=[];self.stack=[]
  for m in re.finditer('\n',text):self.offsets.append(m.end())
 def pos(self):l,c=self.getpos();return self.offsets[l-1]+c
 def handle_starttag(self,t,a):
  a=dict(a)
  if (t=='nav' and 'top-nav' in a.get('class','').split()) or a.get('id')=='mobile-drawer':self.stack.append([t,1,self.pos()])
  elif self.stack and t==self.stack[-1][0]:self.stack[-1][1]+=1
 def handle_endtag(self,t):
  if self.stack and t==self.stack[-1][0]:
   self.stack[-1][1]-=1
   if not self.stack[-1][1]:x=self.stack.pop();self.ranges.append((x[2],self.pos()+len(t)+3))
for p in Path('.').glob('*.html'):
 t=p.read_text();parser=Ranges(t);parser.feed(t)
 for start,end in reversed(parser.ranges):t=t[:start]+t[end:]
 def clean_script(m):
  s=m.group(1)
  if 'function toggleDD' in s or 'function toggleDrop' in s:
   if '/* ── Scroll reveal' in s:s=s[s.index('/* ── Scroll reveal'):]
   elif "window.addEventListener('scroll'" in s:s=s[s.index("window.addEventListener('scroll'"):]
   else:s=''
  return '<script>'+s+'</script>' if s.strip() else ''
 t=re.sub(r'<script>(.*?)</script>',clean_script,t,flags=re.S)
 t=t.replace('href="fase1.html"','href="index.html#fase-1"').replace('diecisiete módulos','dieciocho módulos y un epílogo')
 t=t.replace('Cada pensador tiene un espejo en 2025.','Ideas históricas para examinar problemas del presente.').replace('Cada pensador, cada concepto, tiene un espejo en 2025.','Cada pensador, cada concepto, ofrece una perspectiva para examinar el presente.')
 t=t.replace('Antigüedad griega','Antigüedad y Edad Media').replace('Fase I — Antigüedad','Fase I — Antigüedad y Edad Media')
 t=t.replace('Imaginó un mundo sin Estado y demostró que sería una pesadilla.','Imaginó un mundo sin un poder común y argumentó que la inseguridad amenazaría la convivencia.')
 t=t.replace('Estudios muestran que una fracción creciente de ciudadanos en democracias liberales oculta sus opiniones políticas por miedo a las consecuencias sociales.','Como hipótesis de análisis, la presión social puede llevar a ocultar opiniones; su alcance requiere evidencia específica.')
 t=t.replace('El horizonte del ciclo electoral de cuatro años es el marco temporal más corto de la historia política — y Tocqueville ya lo señaló como un defecto estructural de la democracia.','Los incentivos electorales pueden favorecer resultados inmediatos; esta aplicación contemporánea debe distinguirse del argumento histórico de Tocqueville.')
 t=t.replace('Lees a Smith sin la distorsión neoliberal — que es exactamente lo que él habría pedido.','Distingues el papel del mercado y de las instituciones en Smith. Contrasta ahora sus límites con Marx.')
 if p.name=='hayek-keynes.html':t=t.replace('<!-- HERO SPLIT -->','<h1 class="fp-visually-hidden">Hayek y Keynes: coordinación e intervención</h1>\n<!-- HERO SPLIT -->')
 if p.name in ['mill.html','tocqueville.html']:
  t=t.replace('2025','el presente')
  t=t.replace('<main','<aside class="fp-note">Las conexiones contemporáneas de este módulo son interpretaciones didácticas, no noticias verificadas. Consulta <a href="presente.html">Teoría ↔ Presente</a> para análisis fechados y con fuentes.</aside><main',1)
 t=t.replace('Applies both frameworks where they work. That is real economic literacy.','Distingues ambos marcos y sus límites. Explica qué evidencia te haría cambiar de interpretación.')
 # placeholders for common components, rendered by build.py later
 t=t.replace('<body>','<body>\n<!-- FP:NAV -->',1)
 t=t.replace('</head>','<link rel="stylesheet" href="assets/css/portal.css">\n<script type="module" src="assets/js/common.js"></script>\n</head>')
 t=t.replace('</body>','<!-- FP:FOOTER -->\n</body>')
 if p.name=='index.html':
  t=t.replace('<section class="phases">','<section class="phases" id="aprender">').replace('data-phase="1"','data-phase="1" id="fase-1"')
  t=t.replace('Un portal para entender de dónde vienen las ideas que gobiernan el mundo.','Entender de dónde vienen las ideas para pensar mejor el presente.')
  t=t.replace('<div class="hero-scroll">','<div class="fp-actions"><a class="fp-button" href="#aprender">Empezar a aprender</a><a class="fp-button fp-secondary" href="laboratorio.html">Ponerme a prueba →</a></div><div class="hero-scroll">')
 p.write_text(t)
