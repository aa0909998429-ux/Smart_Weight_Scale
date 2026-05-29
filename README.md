#  Python BLE 智慧體重計直連工具 (Smart Weight Scale)

這是一個基於 Python 與 [`bleak`](https://github.com/hbldh/bleak) 函式庫的低功耗藍牙 (BLE) 體重計連線工具。專為解決體重計「廣播時間短、容易進入省電模式休眠」的問題而設計。

透過預先掃描鎖定 (Scanner) 與快速握手協議，本工具可以實現「閃電直連」，並透過 Nordic UART 服務持續監聽並解析體重數據。

---

##  功能特點

* **閃電直連模式**：先以 `BleakScanner` 快速捕捉廣播包，鎖定目標後立即連線，大幅降低連線失敗率。
* **防休眠機制應對**：包含自動重試邏輯，應對體重計短暫廣播即關機的硬體限制。
* **Nordic UART 支援**：內建針對 Nordic 服務 UUID (`6e400001-...`) 的讀寫與訂閱 (Notify) 處理。
* **萬能解鎖鑰匙**：自動嘗試常見的喚醒指令 (`0x02`, `0x10`, `0x13`)，啟動數據傳輸。

---

##  環境準備

1. **作業系統支援**：Windows 10/11, macOS, Linux
2. **Python 版本**：Python 3.8+
3. **安裝依賴套件**：

```bash
pip install bleak
