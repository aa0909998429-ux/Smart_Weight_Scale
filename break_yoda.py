import asyncio
import traceback
from bleak import BleakScanner, BleakClient, BleakError

# 🎯 Yoda1 地址
ADDRESS = "F0:2C:59:88:77:03"


async def main():
    print("========================================")
    print(f"   🧟 不死鳥計畫：強制突破 Yoda1")
    print(f"   目標: {ADDRESS}")
    print("   程式會不斷重試，直到成功為止！")
    print("========================================")
    print("👉 請務必：踩在體重計上，保持數字亂跳！")

    retry_count = 0

    while True:
        retry_count += 1
        print(f"\n🔄 [第 {retry_count} 次] 嘗試捕捉訊號...", end="", flush=True)

        try:
            # 1. 快速掃描 (只給 3 秒，求快不求久)
            device = await BleakScanner.find_device_by_address(ADDRESS, timeout=3.0)

            if not device:
                print(" ❌ 沒掃到 (請保持喚醒)", end="")
                await asyncio.sleep(0.5)
                continue

            print(" ✅ 鎖定！正在突入...", end="", flush=True)

            # 2. 嘗試連線 (如果這裡失敗，會被下方的 except 抓到，不會崩潰)
            async with BleakClient(device, timeout=5.0) as client:
                print("\n\n🎉🎉🎉 突破成功！連線建立！ 🎉🎉🎉")
                print("========================================")
                print("正在下載體重計的內部構造 (UUID)...")

                # 3. 列出服務 (這是我們要的關鍵資料)
                for service in client.services:
                    print(f"📂 服務 UUID: {service.uuid}")
                    for char in service.characteristics:
                        props = ",".join(char.properties)
                        print(f"   └─ 🔑 特徵值: {char.uuid} [{props}]")
                    print("-" * 20)

                print("========================================")
                print("✅ 構造下載完成！請複製以上內容給我！")
                print("程式將維持連線 10 秒...")
                await asyncio.sleep(10)
                # 任務完成，跳出迴圈
                break

        except Exception as e:
            # 這裡會攔截所有的錯誤 (包含剛剛那個 DeviceNotFound)
            # 我們只印一個驚嘆號，然後立刻重試，不浪費時間
            print(" ⚠️ 脫鉤了 (自動重試中)", end="")
            await asyncio.sleep(0.5)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程式已停止")