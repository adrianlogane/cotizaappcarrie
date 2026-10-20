import json,time,urllib.request,urllib.parse,sys,os
D=sys.argv[1]
src=json.load(open(D+'/comunas.json'))
out_path=D+'/geo.json'
geo=json.load(open(out_path)) if os.path.exists(out_path) else {}
def q(params):
    url='https://nominatim.openstreetmap.org/search?'+urllib.parse.urlencode({**params,'format':'json','limit':1,'countrycodes':'cl'})
    req=urllib.request.Request(url,headers={'User-Agent':'cotizador-carga-chlg/1.0'})
    r=json.load(urllib.request.urlopen(req,timeout=30)); time.sleep(1.05); return r
for reg in src['regiones']:
    for c in reg['comunas']:
        k=reg['region']+'|'+c
        if k in geo: continue
        res=[]
        try:
            res=q({'city':c,'state':reg['region']}) or q({'q':c+', '+reg['region']+', Chile'}) or q({'q':c+', Chile'})
        except Exception as e: print('ERR',k,e)
        if res:
            geo[k]={'lat':float(res[0]['lat']),'lon':float(res[0]['lon']),'name':res[0].get('display_name','')[:80]}
        else: print('MISS',k)
        json.dump(geo,open(out_path,'w'),ensure_ascii=False)
print(len(geo))
