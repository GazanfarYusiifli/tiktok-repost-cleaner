# 🚀 TikTok Automated Repost Cleaner

A fast, automated, and secure Playwright-based tool to remove all your TikTok reposts sequentially in just one click.

---

[🇦🇿 Azərbaycan dilində oxu](#-azərbaycan-dili) | [🇬🇧 Read in English](#-english)

---

## 🇬🇧 English

An open-source automation bot built with **Python & Playwright** that sequentially navigates through all your TikTok reposts and cancels them safely without triggering spam restrictions.

### 🌟 Key Features
- ⚡ **Streamlined Flow**: Opens the first video and streams down using `ArrowDown` without reloading pages.
- 🎯 **Targeted Click Mechanism**: Directly detects TikTok's yellow repost icon (`#FFC300`) and confirmation dialogs.
- 🔒 **100% Privacy & Security**: Runs completely local on your machine. No passwords, tokens, or cookies are uploaded anywhere.
- 🛡️ **Rate-Limit Safe**: Implements human-like randomized delays to protect your TikTok account from shadowbans or temporary restrictions.

### 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GazanfarYusiifli/tiktok-repost-cleaner.git
   cd tiktok-repost-cleaner
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

### 🚀 Usage

1. Run the script:
   ```bash
   python tiktok_repost_cleaner.py
   ```

2. In the browser window that opens:
   - Log into your TikTok account.
   - Go to your profile and switch to the **Reposts** tab.
   - **Click on the very first video** (so it opens in full view).

3. Return to the terminal and press **ENTER**.
4. Sit back and watch the script automatically remove all your reposts one by one!

> **Note on Mobile App:** TikTok mobile apps aggressively cache profile data. After the cleaner finishes on your desktop, it may take 5–15 minutes for the mobile app to sync. You can force sync by going to `Settings and privacy -> Free up space -> Clear cache`.

---

## 🇦🇿 Azərbaycan Dili

TikTok-da repost etdiyiniz bütün videoları avtomatik olaraq tək-tək açıb repostu ləğv edən sürətli və təhlükəsiz Playwright avtomatlaşdırma sistemi.

### 🌟 Xüsusiyyətlər
- ⚡ **Avtomatik Naviqasiya**: Birinci videonu açdıqdan sonra `ArrowDown` axını ilə bütün videoları ardıcıl silir.
- 🎯 **Dəqiq Klik Mexanizmi**: TikTok-un sarı repost ikonu (`#FFC300`) və təsdiq dialoqlarını birbaşa aşkarlayır.
- 🔒 **Təhlükəsizlik**: Şifrənizi və ya kukilərinizi heç bir serverə göndərmir, hər şey lokal olaraq öz brauzerinizdə baş verir.
- 🛡️ **Rate-Limit Dostu**: TikTok-un spam bloklamasına (shadowban) düşməmək üçün təbii gecikmələr tətbiq edir.

### 🛠️ Quraşdırma

1. **Repositoriyanı yükləyin:**
   ```bash
   git clone https://github.com/GazanfarYusiifli/tiktok-repost-cleaner.git
   cd tiktok-repost-cleaner
   ```

2. **Virtual mühiti yaradın və aktivləşdirin:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows üçün: .venv\Scripts\activate
   ```

3. **Lazımi kitabxanaları quraşdırın:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

### 🚀 Necə İstifadə Edilir?

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

## 📄 License
MIT License. Created for educational and personal automation purposes.
