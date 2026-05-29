import asyncio
from bleak import BleakScanner


async def main():
    print("========================================")
    print("   🌐 廣域掃描模式 (修正版)")
    print("========================================")

    print("正在掃描中 (5秒)... 請踩亮體重計！")

    # 掃描
    devices = await BleakScanner.discover(timeout=5.0)

    print(f"\n一共發現 {len(devices)} 個裝置：")
    print("-" * 40)

    found_target = False
    for d in devices:
        # 安全取得名稱
        name = d.name or "Unknown"

        # 移除 rssi 以避免報錯，只印名稱和地址
        print(f"📡 名稱: {name} | 地址: {d.address}")

        # 自動標記疑似目標
        # 注意：有時候它會偽裝成 Unknown
        if "Scale" in name or "JXK" in name or "Yoda" in name:
            print("   ⭐⭐⭐ (疑似目標！)")
            found_target = True

        # 檢查地址是否吻合之前的紀錄
        if d.address == "F0:2C:59:88:77:03":
            print("   ⭐⭐⭐ (地址吻合！抓到了！)")
            found_target = True

    print("-" * 40)
    if not found_target:
        print("❌ 列表中沒看到 Yoda/JXK。請檢查是否有 'Unknown' 的裝置可能是它。")
    else:
        print("✅ 抓到了！")


if __name__ == "__main__":
    asyncio.run(main())