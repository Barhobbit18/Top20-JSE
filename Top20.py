import requests
import lxml.html as lh
import pandas as pd

url='https://www.sashares.co.za/best-shares-to-buy-jse/'

doc = lh.fromstring(requests.get(url).content)
tr = doc.xpath('//tr')

frame=[]
i=0
for t in tr[0]:
    i+=1
    col=t.text_content()
    frame.append((col,[]))

for j in range(1,len(tr)):
    T=tr[j]

    if len(T)!=6:    #if you want to check how must it is [len(T) for T in tr_elements[:10]]
        break
    i=0

    for t in T.iterchildren():
        data=t.text_content()

        frame[i][1].append(data)
        i+=1


Dict={title:column for (title,column) in frame}
df=pd.DataFrame(Dict)
df = df.replace(r'\n','', regex=True)
df.columns=df.columns.str.replace('\n','')
df=df.drop(['BUY NOW'], axis=1)

#print(df)
df.to_csv('Top20.csv')
