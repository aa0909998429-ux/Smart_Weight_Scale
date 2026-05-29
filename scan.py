import asyncio
from bleak import BleakScanner


async def scan():
    print("正在掃描藍牙裝置... 請現在踩亮體重計！")

    # 掃描 10 秒鐘
    devices = await BleakScanner.discover(timeout=10.0)

    print("-" * 30)
    print("發現的裝置如下：")
    for d in devices:
        # 濾掉那些沒有名字的雜訊
        if d.name and d.name != "Unknown":
            print(f"名稱: {d.name} | 地址(Address): {d.address}")

    print("-" * 30)
    print("提示：通常體重計會叫 'HC-08', 'Scale', 'Chipsea', 'OKOK' 或一串亂碼")


if __name__ == "__main__":
    asyncio.run(scan())