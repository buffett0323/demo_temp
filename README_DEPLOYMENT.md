# 音頻評估系統部署指南
# Audio Evaluation System Deployment Guide

## 快速開始 / Quick Start

### 1. 運行部署腳本 / Run Deployment Script
```bash
python deploy.py
```

### 2. 手動啟動 / Manual Start
```bash
# 安裝依賴 / Install dependencies
pip install -r requirements.txt

# 啟動服務器 / Start server
python app.py
```

## 網絡配置 / Network Configuration

### 在您的網絡 140.112.41.51 上運行 / Running on your network 140.112.41.51

1. **確保服務器綁定到所有接口** / Ensure server binds to all interfaces
   - 應用程序已配置為 `host='0.0.0.0'`，允許外部訪問
   - The app is configured with `host='0.0.0.0'` to allow external access

2. **防火牆設置** / Firewall Settings
   ```bash
   # Linux/macOS - 開放端口5324 / Open port 5324
   sudo ufw allow 5324
   
   # 或者使用iptables / Or use iptables
   sudo iptables -A INPUT -p tcp --dport 5324 -j ACCEPT
   ```

3. **訪問地址** / Access URLs
   - 本機訪問: `http://127.0.0.1:5324`
   - 網絡訪問: `http://140.112.41.51:5324`
   - 其他設備: `http://[您的IP]:5324`

## 文件結構 / File Structure
```
demo_temp/
├── app.py                 # Flask服務器主程序
├── deploy.py              # 部署腳本
├── requirements.txt       # Python依賴
├── templates/
│   └── index.html        # 網頁介面
├── Audio/                # 音頻文件目錄
│   ├── 11_orig.wav
│   ├── 11_ref.wav
│   ├── 11_recon_abl.wav
│   ├── 15_orig.wav
│   ├── 15_ref.wav
│   ├── 15_recon_abl.wav
│   ├── 16_orig.wav
│   ├── 16_ref.wav
│   └── 16_recon_abl.wav
└── result/               # 結果保存目錄（自動創建）
```

## 功能特點 / Features

### 1. 音頻播放 / Audio Playback
- 直接在網頁中播放音頻文件
- 支持所有現代瀏覽器
- 無需下載音頻文件

### 2. 評分系統 / Rating System
- 三項評分指標：音色、ADSR、內容相似度
- 1-5分評分系統
- 實時表單驗證

### 3. 數據收集 / Data Collection
- 自動保存評分結果到JSON文件
- 時間戳命名避免覆蓋
- 結構化數據格式

## 故障排除 / Troubleshooting

### 音頻文件無法播放 / Audio files not playing
1. 檢查文件路徑是否正確
2. 確保音頻文件存在於Audio目錄中
3. 檢查文件權限

### 無法從其他設備訪問 / Cannot access from other devices
1. 檢查防火牆設置
2. 確認服務器綁定到0.0.0.0
3. 檢查網絡連接

### 端口被占用 / Port already in use
```bash
# 查找占用端口的進程 / Find process using port
lsof -i :5324

# 終止進程 / Kill process
kill -9 [PID]
```

## 生產環境部署 / Production Deployment

### 使用Gunicorn / Using Gunicorn
```bash
# 安裝Gunicorn / Install Gunicorn
pip install gunicorn

# 啟動服務 / Start service
gunicorn -w 4 -b 0.0.0.0:5324 app:app
```

### 使用Nginx反向代理 / Using Nginx Reverse Proxy
```nginx
server {
    listen 80;
    server_name 140.112.41.51;
    
    location / {
        proxy_pass http://127.0.0.1:5324;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 安全注意事項 / Security Notes

1. **僅用於測試環境** / For testing environment only
2. **不要暴露敏感數據** / Don't expose sensitive data
3. **定期備份結果數據** / Regularly backup result data
4. **考慮使用HTTPS** / Consider using HTTPS for production

## 支持 / Support

如有問題，請檢查：
1. 音頻文件是否完整
2. 網絡連接是否正常
3. 防火牆設置是否正確
4. 端口是否被占用
