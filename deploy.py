#!/usr/bin/env python3
"""
部署腳本 - 在您的網絡上運行音頻評估系統
Deployment script for running the audio evaluation system on your network
"""

import os
import sys
import subprocess
import socket

def get_local_ip():
    """獲取本機IP地址"""
    try:
        # 連接到一個外部地址來獲取本機IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def check_requirements():
    """檢查依賴是否安裝"""
    try:
        import flask
        print("✓ Flask 已安裝")
        return True
    except ImportError:
        print("✗ Flask 未安裝，正在安裝...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        return True

def main():
    print("=== 音頻評估系統部署 ===")
    print("=== Audio Evaluation System Deployment ===\n")
    
    # 檢查依賴
    if not check_requirements():
        print("依賴安裝失敗，請手動安裝：pip install -r requirements.txt")
        return
    
    # 獲取IP地址
    local_ip = get_local_ip()
    
    print(f"本機IP地址: {local_ip}")
    print(f"Local IP: {local_ip}")
    print(f"目標網絡: 140.112.41.51")
    print(f"Target Network: 140.112.41.51")
    print()
    
    print("訪問地址 / Access URLs:")
    print(f"  本機訪問: http://127.0.0.1:5324")
    print(f"  本機訪問: http://localhost:5324")
    print(f"  網絡訪問: http://{local_ip}:5324")
    print(f"  網絡訪問: http://140.112.41.51:5324")
    print()
    
    print("注意事項 / Notes:")
    print("1. 確保防火牆允許端口5324")
    print("   Make sure firewall allows port 5324")
    print("2. 確保Audio資料夾中有音頻文件")
    print("   Make sure audio files are in Audio folder")
    print("3. 按 Ctrl+C 停止服務器")
    print("   Press Ctrl+C to stop the server")
    print()
    
    # 檢查音頻文件
    audio_files = [
        "Audio/11_orig.wav", "Audio/11_ref.wav", "Audio/11_recon_abl.wav",
        "Audio/15_orig.wav", "Audio/15_ref.wav", "Audio/15_recon_abl.wav",
        "Audio/16_orig.wav", "Audio/16_ref.wav", "Audio/16_recon_abl.wav"
    ]
    
    missing_files = []
    for file in audio_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("⚠️  警告：以下音頻文件缺失 / Warning: Missing audio files:")
        for file in missing_files:
            print(f"   - {file}")
        print()
    
    print("正在啟動服務器... / Starting server...")
    print("=" * 50)
    
    # 啟動Flask應用
    os.system("python app.py")

if __name__ == "__main__":
    main()
