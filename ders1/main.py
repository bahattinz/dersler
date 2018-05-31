import json
import os
from collections import namedtuple, Counter
from lxml import etree
from jinja2 import Environment, FileSystemLoader
import webbrowser

CURRENT_FOLDER = os.path.dirname(__file__)

class Kitap(object):
    baslik=""
    basim_yili = 2018
    ozet = ""
    yazar = ""

class JsonIslemleri():
    def create_json(self,data):
        '''
        SERIALIZATION
        '''
        dmp = json.dumps(data,default=lambda x:x.__dict__,ensure_ascii=False)
        print("--->JSON verisi oluşturuldu.")
        self.save(dmp)

    def save(self, data):
        with open(os.path.join(CURRENT_FOLDER,"data.json"),"w",encoding="utf-8") as f:
            f.write(data)
        print("--->JSON verisi kaydedildi.")

    def get_data(self):
        '''
        DESERIALIZATION
        '''
        with open(os.path.join(CURRENT_FOLDER,"data.json"),"r",encoding="utf-8") as f:
            data = f.read()

        result = json.loads(data, object_hook=lambda d:namedtuple("Kitap",d.keys())(*d.values()))
        return result

class XmlIslemleri():
    def create_xml(self,data, root_element):
        root = etree.Element(root_element)
        for d in data:
            item = etree.SubElement(root,d.__class__.__name__)
            for field in vars(d):
                p = etree.SubElement(item,field)
                p.text = str(d.__dict__[field])

        xml_str = etree.tostring(root, encoding="utf-8",pretty_print=True, method="xml").decode()
        print("--->XML verisi oluşturuldu.")
        self.save(xml_str)

    def save(self,data):
        with open(os.path.join(CURRENT_FOLDER,"data.xml"),"w",encoding="utf-8") as f:
            f.write(data)
        print("--->XML verisi kaydedildi.")

class HtmlIslemleri():
    def render_html(self,template,data):
        env = Environment(loader=FileSystemLoader(CURRENT_FOLDER))
        t = env.get_template(template)
        html_string = t.render(title="Merhaba!", kitaplar=data)
        file_name = self.save(html_string)
        self.browse_html(os.path.join(CURRENT_FOLDER,file_name))

    def save(self,data):
        with open(os.path.join(CURRENT_FOLDER,"data.html"),"w",encoding="utf-8") as f:
            f.write(data)
        print("--->HTML verisi kaydedildi.")
        return f.name

    def browse_html(self, template):
        webbrowser.open(template)

def yeni_kayit():
    kitap1 = Kitap()
    kitap1.baslik = "YALNIZ KİTAP"
    kitap1.basim_yili = 2010
    kitap1.yazar =  "Orhan Tüleylioğlu"
    kitap1.ozet = "İnsani gelişimin en temel araçlarından biri Kitap’tır. Nefes almak, yeme içme, neslini sürdürme, kendini geliştirme ne kadar doğal vasıflarımız ise onun araçları da o derece hayati öneme sahiptir."\
                    "Okumadan, düşünmeden, öğrenmeden geçen bir ömür gerçekten yaşanmış sayılamaz” diyor Zeynep Oral."\
                    "Nasıl hava, su, besin bizi hayatta tutuyor ise kitap da o yaşamı sürdürürken bizi gelişerek biz yapan en önemli araçlardan birisidir."\
                    "Orhan Tüleylioğlu’nun Yalnız Kitap isimli 328 sayfalık eserini sizlere sadece 5 ½ sayfada sunar iken tek amacımız dağıtım tarihi sayesinde bir kıvılcım çakmak, 19 Mayıs’ı seçmemiz ise bilhassa gençlere bir mesaj vermek için."\
                    "Ulu Önder Mustafa Kemal Atatürk siz gençlere bu ülkeyi emanet ederken bir de hedef gösterdi."

    kitap2 = Kitap()
    kitap2.baslik = "ZAMANIN DAHA KISA TARİHİ"
    kitap2.basim_yili = 2015
    kitap2.yazar = "Stephen Hawking"
    kitap2.ozet = "Bu hafta bir deha daha ebediyete intikal etti. Bilim dünyasının zaman zaman Einstein ile mukayese ettiği, yüzünde çalışan tek bir kas sayesinde sayısız eserler veren çok değerli bir beyin, çok değerli bir insan."\
                    "Onun en çok ses getiren eseri, A Brief History of Time 14 sayfalık bir özet ile paylaşıyoruz."

    return [kitap1,kitap2]

kitaplar = yeni_kayit()

# js=JsonIslemleri()
# # js.create_json(kitaplar)
# js.get_data()

# x = XmlIslemleri()
# x.create_xml(kitaplar,"Kitaplar")

# htm = HtmlIslemleri()
# htm.render_html(template="template2.html",data=kitaplar)

metin = kitaplar[0].ozet
kelimeler = metin.split()
kelime_sayilari = Counter(kelimeler)
for kelime in kelimeler:
    print("{}:{}".format(kelime,kelime_sayilari[kelime]))
