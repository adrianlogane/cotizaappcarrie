import json,urllib.request,sys,time
D=sys.argv[1]
geo=json.load(open(D+'/geo.json'))
O={'PUD':(-33.4290,-70.7700),'SAI':(-33.5880,-71.6120),'VAP':(-33.0340,-71.6260),'AMB':(-33.3930,-70.7860)}
keys=list(geo)
res={k:{} for k in keys}
for i in range(0,len(keys),80):
    chunk=keys[i:i+80]
    coords=[f"{lo},{la}" for la,lo in O.values()]+[f"{geo[k]['lon']},{geo[k]['lat']}" for k in chunk]
    n=len(O)
    url="https://router.project-osrm.org/table/v1/driving/"+";".join(coords)+"?sources="+";".join(map(str,range(n)))+"&destinations="+";".join(map(str,range(n,n+len(chunk))))+"&annotations=distance,duration"
    r=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'cotizador'}),timeout=60))
    assert r['code']=='Ok',r
    for si,o in enumerate(O):
        for di,k in enumerate(chunk):
            d=r['distances'][si][di]; t=r['durations'][si][di]
            res[k][o]=None if d is None else [round(d/1000),round(t/3600,1)]
    time.sleep(1.5)
json.dump(res,open(D+'/routes.json','w'),ensure_ascii=False)
print('ok',len(res))
