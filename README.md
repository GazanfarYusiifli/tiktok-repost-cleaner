# 🚀 TikTok Repost Cleaner (Avtomatlaşdırılmış Repost Silici)

TikTok-da repost etdiyiniz bütün videoları avtomatik olaraq tək-tək açıb repostu ləğv edən sürətli və təhlükəsiz Playwright avtomatlaşdırma sistemi.

---

## 🌟 Xüsusiyyətlər
- ⚡ **Avtomatik Naviqasiya**: Birinci videonu açdıqdan sonra `ArrowDown` axını ilə bütün videoları ardıcıl silir.
- 🎯 **Dəqiq Klik Mexanizmi**: TikTok-un sarı repost ikonu (`#FFC300`) və təsdiq dialoqlarını birbaşa aşkarlayır.
- 🔒 **Təhlükəsizlik**: Şifrənizi və ya kukilərinizi heç bir serverə göndərmir, hər şey lokal olaraq öz brauzerinizdə baş verir.
- 🛡️ **Rate-Limit Dostu**: TikTok-un spam bloklamasına (shadowban) düşməmək üçün təbii gecikmələr tətbiq edir.

---

## 🛠️ Quraşdırma

### 1. Repositoriyanı yükləyin:
```bash
git clone https://github.com/YOUR_USERNAME/tiktok-repost-cleaner.git
cd tiktok-repost-cleaner
```

### 2. Virtual mühiti yaradın və aktivləşdirin:
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows üçün: .venv\Scripts\activate
```

### 3. Lazımi kitabxanaları quraşdırın:
```bash
pip install -r requirements.txt
playwright install chromium
```

---

## 🚀 Necə İstifadə Edilir?

1. Skripti işə salın:
```bash
python tiktok_repost_cleaner.py
```

2. Açılan brauzer pəncərəsində:
   - TikTok hesabınıza daxil olun.
   - Profilinizə keçib **Reposts** (Yenidən paylaşılanlar) bölməsini açın.
   - **Ən birinci videoya klikləyin** (video ekranda açılsın).

3. Terminala qayıdıb **ENTER** basın.
4. Sistem sonuncu repost silinənə qədər avtomatik şəkildə hamısını ləğv edəcək!

---

## ⚠️ Qeyd
TikTok mobil tətbiqi məlumatları keşləyir. Kompüterdə bütün repostlar silindikdən sonra tətbiqdə görünməsi bir neçə dəqiqə çəkə bilər. Tətbiqdə `Settings -> Free up space -> Clear cache` edərək yeniləyə bilərsiniz.

---

## 📄 Lisenziya
MIT License. Təhsil və fərdi istifadə məqsədilə hazırlanmışdır.
