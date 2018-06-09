import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

CURRENT_FOLDER = os.path.dirname(__file__)

#1. READ FILE
df = pd.read_csv(os.path.join(CURRENT_FOLDER,"Womens Clothing E-Commerce Reviews.csv"))

# 2. NaN VALUES:
# pd.dropna() #eksik değerleri olan tüm satırları bırakacaktır.
# df.isnull() # Bir Boolean değeri döndürecek olursanız, bunun eksik bir değer olup olmadığını size söyler.
# df.dropna(axis=1)
# df.fillna(value)


# 3. PARANTEZER VE VERİYE ERİŞİM
# Süslü ve köşeli parantezler, notasyon

# 4.COLUMN RENAME, REMOVE
df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
df.columns = ['test_age', 'test_favorite_color','test_grade', 'test_name']
df.rename(columns={'age': 'is_just_a_number'}, inplace=True)

df = df.drop(["Unnamed: 0","Clothing ID","Review Text","Division Name","Department Name"],axis=1)
df.columns = [c.replace(" ","_") for c in df.columns] # Kolon isimlerindeki boşluk karakteri kaldırılsın

# 5. SORT
df.Class_Name.sort_values()
df["Class_Name"].sort_values(ascending=False)
df.sort_values(["Class_Name","Age"])

# 6. QUERY(FILTERING)
df.query("Class_Name=='Blouses' & Age==20")
df[df["Age"]<20]

# iloc indeksin sırasıyla, loc indeksin kendisiyle işlem yapmaya olanak verir.

# 7.AXIS
# 0:columns/dikey
# 1:rows/yatay
# df.mean(axis=0)

#8.STRING FUNCTIONS
# Bunlar Series.str. <Function / property> gibi erişilebilir.
df.Class_Name.str.contains("deneme")

# 9.GROUPBY
def age_classifiacation(data):
    age = data["Age"].iloc[0]
    if age<25:
        return "Genç"
    elif age>24 and age<35:
        return "Olgun"
    elif age>34 and age<50:
        return "Orta Yaş"
    elif age>50:
        return "Yaşlı"
    else:
        return "Yok"

urun_siniflari=df.groupby("Class_Name")
urun_siniflari.groups.keys()

yasa_gore_urunler = df.groupby(['Class_Name','Age'])['Rating'].count()
yasa_gore_urunler.reset_index(name="Quantity").head()

urun_gruplari = df.groupby("Class_Name")["Rating"].count().reset_index(name="Quantity")
print(urun_gruplari.sort_values("Quantity"))

yaslara_gore_sayilar = df.groupby("Age")["Rating"].count().reset_index(name="Quantity")
print(type(yaslara_gore_sayilar))
print(yaslara_gore_sayilar.head())
yas_gruplarina_gore_sayilar = yaslara_gore_sayilar.groupby(["Age","Quantity"]).apply(age_classifiacation).reset_index(name="Grup")
print(yas_gruplarina_gore_sayilar.head())
temp = yas_gruplarina_gore_sayilar.groupby("Grup",as_index = False)["Quantity"].sum()
print(temp.head())


data = df.groupby(["Clothing_ID","Class_Name"])["Rating"].count()
print(data.sort_values(ascending=False))


data = df.groupby(["Clothing_ID","Class_Name"])["Rating"]\
.agg({"Positive_Feedback_Count":"count","Rating":"sum"})
print(data.sort_values("Rating",ascending=False).head())
sonuc = data.groupby(level=0).apply(lambda x:100 * x.Positive_Feedback_Count / x.Rating)
print(sonuc.sort_values().head())


# describe: NaN değerlerini hariç, veri kümesinin merkezi eğilimini,
# dağılımını ve şeklini özetleyen tanımlayıcı istatistiktir.
# temp = df.describe()

# head: ilk n satırı döndürür. default olarak n=5'tir.
# temp = df.head()

# temp = len(df[df["Age"]<20])
# temp = len(df.query("Age<20"))
# temp = len(df.query("Age<20 & Class_Name=='Pants'"))
# temp = len(df[df["Age"]<20 & df["Class_Name"]=='Pants'])

# 25-34 yaş arasını seçmek
# temp = df.query("Age>25 & Age<34")
