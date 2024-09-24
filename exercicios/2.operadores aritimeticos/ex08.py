mt = float(input('uma distancia em metros: '))
cm = mt * 100
mm = mt * 1000
km = mt / 1000
hm = mt / 100
dam = mt / 10
dm = mt * 10
print('a medida de {}m corresponde a {}cm e {}mm'.format(mt, cm, mm))
print('{}kilometros\n{}hectometro\n{}decametro\n{}decimetro\n'.format(km, hm, dam, dm))