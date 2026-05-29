import asyncio
from bleak import BleakClient

# 🎯 直接指定地址 (不掃描了，浪費時間)
ADDRESS = "F0:2C:59:88:77:03"

# Nordic UART Service UUIDs
UUID_NOTIFY = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
UUID_WRITE = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

# 萬能鑰匙
MAGIC_KEYS = [bytearray([0x02]), bytearray([0x10]), bytearray([0x13])]


def notification_handler(sender, data):
    print(f"🔥 【數據噴發！】HEX: {data.hex()}")
    if len(data) >= 3:
        val = (data[1] << 8) | data[2]
        print(f"   >>> 重量: {val / 100.0} kg")


async def main():
    print("========================================")
    print(f"   🔫 狙擊模式：直接連線 {ADDRESS}")
    print("   跳過掃描，直接強連！")
    print("========================================")
    print("👉 請現在：踩上體重計，讓數字亂跳，不要停！")

    while True:
        try:
            print("\n🚀 發射連線請求...", end="", flush=True)

            # 【關鍵差異】這裡直接放入地址字串，而不是 device 物件
            # 這會強迫 Windows 重新發起連線搜尋
            async with BleakClient(ADDRESS, timeout=20.0) as client:
                print("\n\n🎉🎉🎉 抓到了！連線成功！ 🎉🎉🎉")
                print("----------------------------------------")

                # 1. 訂閱
                print("👂 開啟監聽...")
                await client.start_notify(UUID_NOTIFY, notification_handler)

                # 2. 發送鑰匙
                print("🔑 發送啟動指令...")
                for key in MAGIC_KEYS:
                    try:
                        await client.write_gatt_char(UUID_WRITE, key)
                        print(".", end="", flush=True)
                    except:
                        pass
                    await asyncio.sleep(0.2)

                print("\n📊 接收數據中... (請保持動作)")

                # 3. 死守連線
                while client.is_connected:
                    await asyncio.sleep(1)

        except Exception as e:
            # 失敗了就印一個點，立刻重試
            print(".", end="", flush=True)
            await asyncio.sleep(0.5)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程式停止")