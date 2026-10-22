import sys; sys.path.insert(0,'/workspace/sites/_kit'); from kit import *
FRESHA='https://www.fresha.com/lvp/princess-pro-nails-south-vermont-avenue-los-angeles-30G1wv'
s=Site(slug='princess-pro-nails',name='Princess Pro Nails',tel='tel:+13239716340',phone='(323) 971-6340',ig='https://www.instagram.com/princesspronails/',igh='@princesspronails',
 addr_q='6220+S+Vermont+Ave+Los+Angeles+CA+90044',theme='#20121F',mark='Princess Pro <span>Nails</span>',
 navlinks=[('#services','Services'),('#sets','Sets'),('visit/','Visit')],
 font_files=[('Unbounded','unbounded-700-800','700 800'),('DM Sans','dm-sans-400','400 500')],
 ld={"@type":"NailSalon","telephone":"+1-323-971-6340","address":{"@type":"PostalAddress","streetAddress":"6220 S Vermont Ave","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90044","addressCountry":"US"},"areaServed":"South Los Angeles"})
fr=lambda c='btn btn-l',t='Book on Fresha':f'<a class="{c}" href="{FRESHA}" target="_blank" rel="noopener">{t}<span class="sr"> (opens Fresha)</span></a>'
HRS='Mon-Sat 9 AM-6:30 PM, Sun 9 AM-6 PM'
bulbs=lambda n,cls='':''.join(f'<i class="b{cls}" data-i="{i}"></i>' for i in range(n))
def footer():
  return f'''<footer class="foot"><div class="wrap"><div class="closing" aria-hidden="true">{bulbs(10)}</div><p class="close-line" data-close aria-live="polite">Hours per Google Maps: {HRS}. Call to confirm.</p>
<p class="f-name">Princess Pro Nails</p><p>6220 S Vermont Ave, Los Angeles 90044. <a href="{s.tel}">{s.phone}</a>.</p>
<div class="ctas">{s.call("btn btn-p btn-sm")}{fr("btn btn-l btn-sm")}{s.igb("btn btn-l btn-sm",s.igh)}</div>
<p class="fine">The vanity images are AI-generated illustrative scenes, not photos of Princess Pro Nails or its work. Services and hours come from public listings; call to confirm. Demo site, © 2026 Princess Pro Nails.</p></div></footer>'''
s.footer=footer
ALT="Illustrative: a vanity mirror ringed with warm globe bulbs reflecting a Los Angeles street at dusk. AI-generated, not a photo of Princess Pro Nails."
SV=['Gel nails','Acrylic nails','Manicure',"Men's manicure",'Pedicure','Spa pedicure','Nail art']
svc=''.join(f'<li><i class="b on" aria-hidden="true"></i>{x}</li>' for x in SV)
mir=''.join(f'<li class="m m{i}"><div class="mf">{bulbs(6)}<span>Your sets go here</span></div></li>' for i in (1,2,3))
home=f'''<section class="hero" aria-labelledby="h1"><div class="hero-img">{s.hero_pic(ALT)}</div><span class="ill">Illustrative scene · not Princess Pro Nails</span>
<div class="hero-in"><p class="eyebrow">6220 S Vermont Ave · South LA</p><h1 id="h1">Princess<br>Pro Nails</h1>
<p class="sub">Nail salon on S Vermont Ave. Gel, acrylic, manicures, pedicures and nail art.</p><div class="ctas">{s.call()}{fr()}{s.igb()}</div></div></section>
<section class="sec" id="services" aria-labelledby="svc-h"><div class="wrap two"><div><h2 id="svc-h">Services</h2><p class="lede">Per the salon's Fresha listing. Call to confirm, and for pricing.</p><div class="ctas">{s.call()}{fr()}</div></div>
<div class="mirror-narrow"><ul class="svc">{svc}</ul></div></div></section>
<section class="sec alt" id="sets" aria-labelledby="sets-h"><div class="wrap"><h2 id="sets-h">Your sets go here</h2><p class="lede">These mirrors wait for the salon's own sets. Recent work is on Instagram.</p><ul class="mirrors">{mir}</ul><div class="ctas">{s.igb("btn btn-l","See "+s.igh)}</div></div></section>
<section class="sec" aria-labelledby="visit-h"><div class="wrap two"><div><h2 id="visit-h">6220 S Vermont Ave</h2><address>Princess Pro Nails<br>6220 S Vermont Ave<br>Los Angeles, CA 90044</address><div class="ctas">{s.dirb("btn btn-p")}{s.call("btn btn-l")}</div></div>
<div><ol class="week" aria-label="Weekly hours per Google Maps">{"".join(f'<li data-d="{i}"><i class="b on" aria-hidden="true"></i><b>{d}</b><span>{h}</span></li>' for i,(d,h) in enumerate([("Mon","9-6:30"),("Tue","9-6:30"),("Wed","9-6:30"),("Thu","9-6:30"),("Fri","9-6:30"),("Sat","9-6:30"),("Sun","9-6")]))}</ol><p class="muted">Hours per Google Maps. Call to confirm.</p></div></div></section>'''
rows=hours_rows([(d,'9 AM - 6:30 PM') for d in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']]+[('Sunday','9 AM - 6 PM')])
visit=f'''<section class="phero"><div class="wrap"><p class="eyebrow">Visit</p><h1>6220 S Vermont Ave</h1><address>Princess Pro Nails<br>6220 S Vermont Ave<br>Los Angeles, CA 90044<br><a href="{s.tel}">{s.phone}</a></address><div class="ctas">{s.dirb("btn btn-p")}{s.call("btn btn-l")}{fr()}</div></div></section>
<section class="sec"><div class="wrap two"><div class="card"><h2>Hours</h2><table class="hours"><thead><tr><th scope="col">Day</th><th scope="col">Listed hours</th></tr></thead><tbody>{rows}</tbody></table><p class="muted">Per Google Maps. Call to confirm.</p></div>
<div class="card"><h2>Getting here</h2><p>On S Vermont Ave in South LA (ZIP 90044).</p><p>Parking and walk-ins: call to ask.</p><p><a href="{s.MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></p></div></div></section>'''
nf=f'<section class="phero"><div class="wrap"><h1>Lights out here</h1><p>That page doesn\'t exist.</p><div class="ctas"><a class="btn btn-l" href="{s.B}">Back home</a>{s.call()}</div></div></section>'
s.write([('','Princess Pro Nails | Nail Salon on S Vermont Ave, South LA','Princess Pro Nails, 6220 S Vermont Ave, Los Angeles 90044. Gel, acrylic, manicures, pedicures and nail art. Call (323) 971-6340 or book on Fresha.',home,'',s.preload()),
 ('visit/','Hours & Directions | Princess Pro Nails, South LA','Princess Pro Nails is at 6220 S Vermont Ave, Los Angeles 90044. Listed hours Mon-Sat 9-6:30, Sun 9-6. Call (323) 971-6340 to confirm.',visit,'visit/','')],nf)
open(s.R+'assets/css/site.css','w').write(BASE_CSS+open(s.R+'src/site.css').read())
