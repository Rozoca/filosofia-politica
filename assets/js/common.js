import {change,notice,read} from './store.js';
read();
const nav=document.querySelector('.fp-nav'),toggle=document.querySelector('.fp-menu');
function close(){nav?.classList.remove('fp-open');toggle?.setAttribute('aria-expanded','false');}
toggle?.addEventListener('click',()=>{const open=nav.classList.toggle('fp-open');toggle.setAttribute('aria-expanded',String(open));});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('fp-open')){close();toggle.focus();}});
document.addEventListener('click',e=>{if(nav&&!nav.contains(e.target))close();});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
const module=document.body.dataset.module;
if(module){change(s=>{s.visits[module]=new Date().toISOString();});}
// Expose state of historical disclosure controls without changing their behavior.
document.querySelectorAll('.acc-trigger,.way-trigger').forEach((el,i)=>{if(el.tagName!=='BUTTON'){el.setAttribute('role','button');el.tabIndex=0;el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();el.click();}});}el.setAttribute('aria-expanded','false');const panel=el.nextElementSibling;if(panel){panel.id ||= `fp-disclosure-${i}`;el.setAttribute('aria-controls',panel.id);}new MutationObserver(()=>el.setAttribute('aria-expanded',String(el.classList.contains('open')))).observe(el,{attributes:true,attributeFilter:['class']});});
document.querySelectorAll('.tab-btn').forEach(el=>{el.setAttribute('aria-pressed',String(el.classList.contains('active')));new MutationObserver(()=>el.setAttribute('aria-pressed',String(el.classList.contains('active')))).observe(el,{attributes:true,attributeFilter:['class']});});
if(notice()){const p=document.createElement('p');p.className='fp-note';p.setAttribute('role','status');p.textContent=notice();nav?.after(p);}
