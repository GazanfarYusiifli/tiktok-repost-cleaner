import asyncio
import os
import sys
from pathlib import Path
from playwright.async_api import async_playwright

USER_DATA_DIR = Path(__file__).parent / "tiktok_browser_profile"

async def no_refresh_stable_cleaner():
    print("=" * 65)
    print("🛡️ TikTok Sabit Repost Təmizləyici (Səhifəni Yeniləmədən)")
    print("=" * 65)

    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            channel="chrome",
            viewport={"width": 1280, "height": 850},
            args=["--disable-blink-features=AutomationControlled", "--start-maximized"]
        )

        page = context.pages[0] if context.pages else await context.new_page()

        print("\n🌐 TikTok açılır...")
        await page.goto("https://www.tiktok.com", wait_until="domcontentloaded")

        print("\n" + "-" * 60)
        print("👉 TƏLİMAT:")
        print("1. Profilinizdə 'Reposts' bölməsinə keçin.")
        print("2. 1-ci videonu açın (video açıq qalsın).")
        print("3. Buraya qayıdıb ENTER basın.")
        print("-" * 60 + "\n")

        await asyncio.to_thread(input, "1-ci video açıqdırsa, ENTER basın... ")

        print("\n🚀 Fasiləsiz təmizləmə başladı...")

        deleted_count = 0
        total_checked = 0
        stuck_counter = 0
        last_url = ""

        while True:
            total_checked += 1
            current_url = page.url

            # Eyni videoda qalıbmı yoxlayırıq
            if current_url == last_url and "/video/" in current_url:
                stuck_counter += 1
            else:
                stuck_counter = 0
                last_url = current_url

            # Əgər video ilişibsə və ya növbəti video gəlmirsə:
            if stuck_counter >= 3:
                print("⚠️ Video axını ilişib, təkrar ArrowDown və səhifə daxili silkələmə edilir...")
                await page.keyboard.press("ArrowDown")
                await asyncio.sleep(1.0)
                if stuck_counter >= 6:
                    print("\n✅ Artıq növbəti video gəlmir, bütün repostlar sona çatdı!")
                    break

            # Sarı ikonu gözləyirik (lazım gələrsə 2 saniyəyə qədər)
            yellow_locator = page.locator('path[fill="#FFC300"], path[fill="#ffc300"]').first
            is_found = False

            try:
                await yellow_locator.wait_for(state="attached", timeout=1800)
                is_found = True
            except:
                is_found = False

            if is_found:
                try:
                    # 1. Force click
                    btn = yellow_locator.locator('xpath=./ancestor::button | ./ancestor::div[contains(@class, "Button") or contains(@role, "button")] | ./ancestor::svg').first
                    try:
                        await btn.click(force=True, timeout=800)
                    except:
                        pass

                    # 2. Fiziki kursor və basılma
                    box = await yellow_locator.bounding_box()
                    if box:
                        x = box['x'] + box['width'] / 2
                        y = box['y'] + box['height'] / 2
                        await page.mouse.move(x, y)
                        await asyncio.sleep(0.1)
                        await page.mouse.down()
                        await asyncio.sleep(0.08)
                        await page.mouse.up()

                    # 3. 'Remove repost'
                    await asyncio.sleep(0.2)
                    remove_loc = page.locator('text="Remove repost"').first
                    if await remove_loc.count() > 0 and await remove_loc.is_visible():
                        await remove_loc.click(force=True, timeout=800)

                    deleted_count += 1
                    print(f"🗑️ [{deleted_count}] Repost ləğv edildi! (Video #{total_checked})")
                    await asyncio.sleep(0.6)
                except Exception:
                    pass
            else:
                print(f"⏩ Video #{total_checked}: Sarı repost ikonu tapılmadı.")

            # HƏLLİ: Səhifəni refresh ETMİRİK!
            # Sadəcə hər videodan sonra ArrowDown basırıq, əgər növbəti video gəlmirsə 2-ci dəfə ArrowDown basırıq
            await page.keyboard.press("ArrowDown")
            await asyncio.sleep(1.2)

        print("\n" + "=" * 65)
        print(f"🎉 BÜTÜN PROSES TAMAMLANDI!")
        print(f"Cəmi yoxlanılan video: {total_checked}")
        print(f"Cəmi silinən repost: {deleted_count}")
        print("=" * 65)
        await context.close()

if __name__ == "__main__":
    try:
        asyncio.run(no_refresh_stable_cleaner())
    except KeyboardInterrupt:
        print("\n🛑 Dayandırıldı.")
        sys.exit(0)
