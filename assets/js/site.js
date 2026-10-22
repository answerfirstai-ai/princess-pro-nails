document.querySelectorAll('.mnav a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
// Signature: footer bulbs dim one per hour toward closing time (LA time); today's day is lit in the week.
(()=>{const C=[18.5,18.5,18.5,18.5,18.5,18.5,18],O=9;const p=new Intl.DateTimeFormat('en-US',{timeZone:'America/Los_Angeles',weekday:'short',hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date());
const d=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(p.find(x=>x.type=='weekday').value),h=(+p.find(x=>x.type=='hour').value%24)+(+p.find(x=>x.type=='minute').value)/60;
const w=document.querySelector(`.week li[data-d="${d}"]`);if(w)w.classList.add('today');
const bs=[...document.querySelectorAll('.closing .b')],t=document.querySelector('[data-close]');if(!bs.length||d<0)return;const c=C[d];let on,msg;
if(h<O){on=0;msg='Closed now. Listed to open at 9 AM. Call to confirm.'}else if(h>=c){on=0;msg='Closed now. Listed to open tomorrow at 9 AM. Call to confirm.'}
else{const left=c-h;on=Math.max(1,Math.min(bs.length,Math.ceil(left)));const ct=c==18.5?'6:30 PM':'6 PM';msg=`Listed as open until ${ct}. ${on} bulb${on>1?'s':''} left. Call to confirm.`}
bs.forEach((b,i)=>b.classList.toggle('off',i>=on));t.textContent=msg;})();
document.addEventListener('keydown',e=>{if(e.key!=='Escape')return;document.querySelectorAll('details.mnav[open]').forEach(d=>{d.open=false;d.querySelector('summary').focus()})});
document.querySelectorAll('details.mnav').forEach(d=>{const m=d.querySelector('summary');const u=()=>{m.setAttribute('aria-expanded',d.open);m.setAttribute('aria-label',d.open?'Close menu':'Open menu')};u();d.addEventListener('toggle',u)});
