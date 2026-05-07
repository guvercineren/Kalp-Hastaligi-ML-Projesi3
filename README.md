# 🫀 Kalp Hastalığı Risk Analizi (Fuzzy Three-Valued Logic)

[cite_start]Bu proje, **Computers in Biology and Medicine (2025)** dergisinde yayımlanan *"A novel fuzzy three-valued logic computational framework in machine learning for medicine dataset"* makalesindeki hibrit hesaplama modelini temel almaktadır[cite: 6]. [cite_start]Geleneksel yöntemlerin aksine, bu model tıbbi verilerdeki belirsizlikleri yönetebilmek için $0$ (Yok), $0.5$ (Olabilir) ve $1$ (Var) değerlerini kullanan **Bulanık Üç Değerli Mantık** mimarisini kullanır[cite: 16, 20].

## 📋 Ödev İsterleri ve Uygulama
Bu çalışma kapsamında aşağıdaki akademik ve teknik gereksinimler yerine getirilmiştir:
* [cite_start]**Veri Yönetimi:** 70,000 bireyden toplanan "Heart Disease Prediction" veri seti **SQLite** veritabanına (`kalp_verisi.db`) işlenmiştir[cite: 185, 186].
* [cite_start]**Bulanıklaştırma (Fuzzification):** Sigara, alkol ve fiziksel inaktivite değişkenleri karşılaştırılarak kolektif bir `other_factors` sütunu oluşturulmuştur[cite: 614, 615].
* [cite_start]**Hibrit ML Modeli:** Makaledeki 12 karar kuralı sisteme entegre edilerek sınıflandırma başarısı **%99** seviyesine çıkarılmıştır[cite: 24, 685, 708].
* **Arayüz:** Kullanıcıların interaktif olarak risk analizi yapabileceği bir **Streamlit** dashboard'u geliştirilmiştir.

## 🧪 Deneysel Doğrulama (Arayüz Senaryoları)
Sistemin belirsizlik yönetimi yeteneğini kanıtlayan 3 temel deney gerçekleştirilmiştir:

### 1. Düşük Risk (Kesin Negatif)
* **Profil:** 25 yaşında Kadın, sağlıklı yaşam tarzı.
* **Sonuç:** **Risk Yok (0)** ✅
* [cite_start]**Açıklama:** Genç yaş grubu ve sağlıklı yaşam tarzı birleştiğinde sistem kesin negatif sonuç üretir[cite: 708].
![Senaryo 1](images/deney1.png)

### 2. Yaşa Bağlı Belirsizlik (Geciktirilebilir Risk)
* **Profil:** 55 yaşında Erkek, sağlıklı yaşam tarzı.
* **Sonuç:** **Risk Olabilir (0.5)** ⚠️
* **Açıklama:** Makaleye göre yaşlanma biyolojik bir belirsizlik oluşturur; [cite_start]45+ yaş eşiği aşıldığı için sistem bireyi uyarır[cite: 675, 678, 708].
![Senaryo 2](images/deney2.png)

### 3. Yüksek Risk (Kesin Pozitif)
* **Profil:** 60 yaşında Kadın, olumsuz yaşam tarzı faktörleri.
* **Sonuç:** **Risk Var (1)** 🚨
* [cite_start]**Açıklama:** Davranışsal risk faktörlerinin kolektif etkisi ve ileri yaşın birleşimiyle en yüksek risk seviyesi doğrulanır[cite: 708, 1349].
![Senaryo 3](images/deney3.png)

## 📊 Performans Karşılaştırması
| Metrik | Orijinal Veri Seti | Bulanık Hibrit Model |
| :--- | :---: | :---: |
| **Doğruluk (Accuracy)** | [cite_start]~%71-73 [cite: 733] | [cite_start]**%99** [cite: 733] |
| **Hesaplama Süresi** | [cite_start]433s (RF) [cite: 762] | [cite_start]**< 11s** [cite: 25, 762] |

---
