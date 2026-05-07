import streamlit as st

# Sayfa yapılandırması (Görseldeki gibi başlık ve ikon)
st.set_page_config(page_title="Kalp Hastalığı Risk Analizi", page_icon="🫀", layout="centered")

# CSS ile özel stil verme (Buton renkleri ve metin düzenlemeleri)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Başlık Bölümü
st.title("🫀 Kalp Hastalığı Risk Analizi")
st.markdown("##### Bulanık Üç Değerli Mantık (Fuzzy Three-Valued Logic) Karar Destek Sistemi")
st.write("Lütfen risk analizi için aşağıdaki bilgileri doldurun:")

# Giriş Alanları - Yan yana kolonlar
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Cinsiyetiniz", options=["Kadın", "Erkek"])
    gender_val = 1 if gender == "Kadın" else 2

with col2:
    age = st.number_input("Yaşınız", min_value=1, max_value=120, value=55)

st.markdown("---")

# Yaşam Tarzı Faktörleri Bölümü
st.subheader("Yaşam Tarzı Faktörleri")

smoke = st.radio("Sigara kullanıyor musunuz?", options=["Hayır", "Evet"], horizontal=True)
alco = st.radio("Alkol kullanıyor musunuz?", options=["Hayır", "Evet"], horizontal=True)
active = st.radio("Düzenli fiziksel aktivite yapıyor musunuz?", options=["Hayır", "Evet"], index=1, horizontal=True)

# Değerleri sayısal forma çevirme
x = 1 if smoke == "Evet" else 0
y = 1 if alco == "Evet" else 0
not_z = 0 if active == "Evet" else 1

# Bulanıklaştırma Mantığı (Fuzzification) [cite: 1581, 1603]
if x == y == not_z:
    other_factors = float(x)
else:
    other_factors = 0.5

# Tahmin Butonu
if st.button("Riski Hesapla"):
    st.markdown("---")
    st.subheader("Tahmin Sonucu")
    
    # Karar Mekanizması (Makale Tablo 13'teki 12 Kural) 
    result_text = ""
    status = "" # success, warning, error
    
    if gender_val == 1: # Kadın
        if age < 55:
            if other_factors == 0: 
                result_text = "Risk Yok (0): Sağlıklı görünüyorsunuz."
                status = "success"
            elif other_factors == 0.5: 
                result_text = "Risk Olabilir (0.5): Yaşam tarzınıza dikkat etmelisiniz."
                status = "warning"
            else: 
                result_text = "Risk Var (1): Risk faktörleri mevcut! Bir uzmana başvurun."
                status = "error"
        else: # >= 55
            if other_factors == 1: 
                result_text = "Risk Var (1): Yüksek risk grubu! Lütfen bir uzmana başvurun."
                status = "error"
            else: 
                result_text = "Risk Olabilir (0.5): Yaş faktörü nedeniyle dikkatli olmalısınız."
                status = "warning"
    else: # Erkek
        if age < 45:
            if other_factors == 0: 
                result_text = "Risk Yok (0): Mevcut verilerle risk saptanmadı."
                status = "success"
            elif other_factors == 0.5: 
                result_text = "Risk Olabilir (0.5): Bazı risk faktörleri tespit edildi."
                status = "warning"
            else: 
                result_text = "Risk Var (1): Risk faktörleri yüksek! Kontrol şart."
                status = "error"
        else: # >= 45
            if other_factors == 1: 
                result_text = "Risk Var (1): Risk faktörleri mevcut! Lütfen sağlığınıza dikkat edin."
                status = "error"
            else: 
                result_text = "Risk Olabilir (0.5): Yaş ve yaşam tarzı nedeniyle orta derece risk."
                status = "warning"

    # Sonucu görseldeki gibi göster
    if status == "success":
        st.success(f"✅ {result_text}")
    elif status == "warning":
        st.warning(f"⚠️ {result_text}")
    else:
        st.error(f"🚨 {result_text}")
    
    # Teknik Bilgi (Opsiyonel)
    with st.expander("Teknik Detayları Gör"):
        st.write(f"Hesaplanan 'Diğer Faktörler' (Fuzzy Value): {other_factors}")
        st.write("Bu sonuç makaledeki 'Hybrid Fuzzy Three-Valued' modeline dayanmaktadır. [cite: 1588]")