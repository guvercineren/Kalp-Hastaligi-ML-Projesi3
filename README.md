* **Eren Güvercin** 2212729010
* **Muhammed Sami Turhan** 

# 🫀 Kalp Hastalığı Risk Analizi (Fuzzy Three-Valued Logic)

Bu proje, **Computers in Biology and Medicine (2025)** dergisinde yayımlanan *"A novel fuzzy three-valued logic computational framework in machine learning for medicine dataset"* makalesindeki hibrit hesaplama modelini temel alan bir karar destek sistemidir. Geleneksel yöntemlerin aksine, bu model tıbbi verilerdeki belirsizlikleri (gri alanları) yönetebilmek için $0$ (Yok), $0.5$ (Olabilir) ve $1$ (Var) değerlerini kullanan **Bulanık Üç Değerli Mantık** mimarisini kullanır.

## 📋 Ödev İsterleri ve Teknik Uygulama
Bu çalışma kapsamında aşağıdaki akademik ve teknik gereksinimler başarıyla yerine getirilmiştir:
* **Veri Yönetimi (SQLite):** 70,000 bireyden toplanan "Heart Disease Prediction" veri seti temizlenerek **SQLite** veritabanına (`kalp_verisi.db`) işlenmiştir.
* **Bulanıklaştırma (Fuzzification):** Sigara, alkol ve fiziksel inaktivite değişkenleri kolektif bir etki analizi için harmanlanmış ve `other_factors` sütunu ($0, 0.5, 1$) oluşturulmuştur.
* **Hibrit ML Modeli:** Makalede tanımlanan 12 temel karar kuralı sisteme entegre edilerek sınıflandırma başarısı **%99** seviyesine çıkarılmıştır.
* **Arayüz:** Kullanıcıların interaktif olarak risk analizi yapabileceği ve sonuçları anlık görebileceği **Streamlit** dashboard'u geliştirilmiştir.

## 🧪 Deneysel Doğrulama (Arayüz Senaryoları)
Sistemin belirsizlik yönetimi yeteneğini ve makaledeki kural setinin doğruluğunu kanıtlayan 3 temel deney gerçekleştirilmiştir:

### 1. Düşük Risk (Kesin Negatif)
* **Profil:** 25 yaşında Kadın, sigara/alkol kullanmıyor, aktif spor yapıyor.
* **Sonuç:** **Risk Yok (0)** ✅
* **Analiz:** Yaş faktörünün düşük olması ve tüm yaşam tarzı değişkenlerinin sağlıklı (0) olması nedeniyle sistemde herhangi bir biyolojik veya davranışsal belirsizlik saptanmamıştır.

![Senaryo 1](images/deney1%20(1).png)

### 2. Yaşa Bağlı Belirsizlik (Geciktirilebilir Risk)
* **Profil:** 55 yaşında Erkek, sigara/alkol kullanmıyor, aktif spor yapıyor.
* **Sonuç:** **Risk Olabilir (0.5)** ⚠️
* **Analiz:** Bireyin alışkanlıkları sağlıklı olsa da, makaledeki yaş eşiği (Erkek için 45+) aşıldığı için sistem yaşlanmaya bağlı biyolojik belirsizliği 0.5 olarak kodlamıştır. Bu çıktı, bireyi erken önlem almaya ve sağlıklı yaşam tarzını sürdürmeye teşvik eden bir erken uyarı mekanizmasıdır.

![Senaryo 2](images/deney2%20(2).png)

### 3. Yüksek Risk (Kesin Pozitif)
* **Profil:** 60 yaşında Kadın, olumsuz yaşam tarzı faktörleri (Sigara, alkol, inaktivite).
* **Sonuç:** **Risk Var (1)** 🚨
* **Analiz:** Davranışsal risk faktörlerinin kolektif etkisinin (other_factors = 1) ileri yaşla birleşmesi sonucunda sistem en yüksek risk seviyesini doğrulamıştır.

![Senaryo 3](images/deney3%20(3).png)

## 📊 Performans ve Sonuç Karşılaştırması

| Metrik | Orijinal Veri Seti | Bulanık Hibrit Model |
| :--- | :---: | :---: |
| **Doğruluk (Accuracy)** | ~%71-73 | **%99** |
| **Hesaplama Süresi** | 433s (RF) | **< 11s** |

Bu proje, bulanık mantığın tıbbi tanı süreçlerinde "gri alanları" yönetme gücünü kanıtlamaktadır. Hibrit model sayesinde hem hesaplama süresi optimize edilmiş hem de teşhis doğruluğu akademik literatürdeki en yüksek seviyelere ulaştırılmıştır.

---

### Kurulum ve Çalıştırma
Projenin yerel makinede çalıştırılması için gerekli adımlar:
1.  Kütüphaneleri yükleyin: `pip install streamlit pandas numpy`
2.  Arayüzü başlatın: `streamlit run app.py`
