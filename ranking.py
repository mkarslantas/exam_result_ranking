import numpy as np # Numpy, Python programlama dili için büyük, çok boyutlu dizileri ve matrisleri destekleyen, bu diziler üzerinde çalışacak üst düzey matematiksel işlevler ekleyen bir kitaplıktır
import pandas as pd # Pandas, veri işlemesi ve analizi için Python programlama dilinde yazılmış olan bir yazılım kütüphanesidir

df = pd.read_excel("çads_sonuçlar.xlsx")

df.columns = ['Adı Soyadı', 'Email', 'GSM', 'Kurum', 'Sınıf', 'Doğru', 'Yanlış', 'LOGIN']

df_0 = df
df_1 = df_0[df_0['Sınıf'] == 1]
df_2 = df_0[df_0['Sınıf'] == 2]
df_3 = df_0[df_0['Sınıf'] == 3]
df_4 = df_0[df_0['Sınıf'] == 4]

# Genel sıralama 'ascending=False' argümanı, sıralamanın büyükten küçüğe olmasını sağlar. Bu durumda, daha çok doğru ve daha az yanlış yapan öğrencinin daha yüksek bir sıralama almasını sağlar. 
df_1 = df_1.sort_values(['Doğru', 'Yanlış'], ascending=[False, True])
df_2 = df_2.sort_values(['Doğru', 'Yanlış'], ascending=[False, True])
df_3 = df_3.sort_values(['Doğru', 'Yanlış'], ascending=[False, True])
df_4 = df_4.sort_values(['Doğru', 'Yanlış'], ascending=[False, True])

# Not: groupby().ngroup() fonksiyonu, grupları 0'dan başlayarak numaralandırır. 'ascending=False' parametresi, indekslerin atandığı sıralamayı tersine çevirir. Bu, en yüksek değerli grup için 0'ın, daha sonra gelen gruplar için artan sayıların atanmasını sağlar. Bu nedenle, sıralamanın 1'den başlamasını sağlamak için sonuçlarına 1 ekliyoruz.
df_1['Genel Sıra'] = df_1.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1
df_2['Genel Sıra'] = df_2.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1
df_3['Genel Sıra'] = df_3.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1
df_4['Genel Sıra'] = df_4.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1

# Kurum içi sıralama : her kurum için 'Doğru' ve 'Yanlış' değerlerine göre ayrı ayrı sıralama yapar ve her kurumda 1'den başlar:
df_1['Kurum Sıra'] = df_1.groupby('Kurum').apply(lambda x: x.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1).reset_index(level=0, drop=True)
df_2['Kurum Sıra'] = df_2.groupby('Kurum').apply(lambda x: x.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1).reset_index(level=0, drop=True)
df_3['Kurum Sıra'] = df_3.groupby('Kurum').apply(lambda x: x.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1).reset_index(level=0, drop=True)
df_4['Kurum Sıra'] = df_4.groupby('Kurum').apply(lambda x: x.groupby(['Doğru', 'Yanlış']).ngroup(ascending=False) + 1).reset_index(level=0, drop=True)


new_df = pd.concat([df_1, df_2, df_3, df_4], ignore_index=True)
new_df
