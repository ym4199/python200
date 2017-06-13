solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해황성']
solar2=['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

solardict={} # 빈사전형을 생성한다.
for i , k in enumerate(solarsys): # enumerate로 index와 string을 받는다
    val = solar2[i]
    solardict[k] = val # index에 따라 짝을 지어준다(리스트는 순서가 있으니까 가능)

print(solardict)
# 사전형이기 때문에 순서가 없다.