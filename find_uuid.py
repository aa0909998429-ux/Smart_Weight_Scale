import asyncio
from bleak import BleakClient

# ==========================================
# 【請把這裡改成你剛剛掃到的地址】
ADDRESS = "A4:C1:38:12:34:56"
# ==========================================

# 這是 Chipsea/OKOK 體重計最常見的 UUID
# 用來告訴它：「我要訂閱數據通知」
NOTIFY_UUID = "0000fff4-0000-1000-8000-00805f9b34fb"

def notification_handler(sender, data):
    """
    這段程式碼會在「每次收到數據」時自動執行
    """
    hex_data = data.hex()
    print(f"【收到數據】: {hex_data}")

    # --- 簡單解析嘗試 (你可以觀察這段數值跟體重的關係) ---
    # 這裡只是範例，不同廠牌解碼方式不同
    try:
        # 假設數據長度夠長
        if len(data) >= 5:
            # 很多體重計的數據在第 2,3 byte
            # 試著把 Hex 轉成十進位
            val = int(hex_data[4:8], 16)
            print(f" -> 嘗試解碼數值: {val} (可能是重量x10或x100)")
    except:
        pass

async def main():
    print(f"正在連線到 {ADDRESS} ...")
    print("如果是第一次連線，可能會花個 5~10 秒，請耐心等候。")

    try:
        async with BleakClient(ADDRESS) as client:
            print("連線成功！(請站上體重計動一動)")

            # 開啟通知 (訂閱數據流)
            await client.start_notify(NOTIFY_UUID, notification_handler)

            # 讓程式持續跑 60 秒，你可以盡情測試
            await asyncio.sleep(60)

            print("測試結束，斷開連線。")
    except Exception as e:
        print(f"連線發生錯誤: {e}")

if __name__ == "__main__":
    asyncio.run(main())