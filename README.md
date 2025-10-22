# Telegram Periodic Sender (Template)

**Mục đích:** gửi tin nhắn định kỳ tới 1 `6794824681` (chỉ gửi cho chính bạn / nhóm bạn kiểm soát).  
**Cảnh báo:** Không dùng để spam. Nếu token bị lộ, revoke ngay trong @BotFather.

## Files
- `bot.py` - script chính (dùng biến môi trường)
- `requirements.txt` - dependencies
- `.gitignore`

## Cấu hình (khuyến nghị)
**Không** ghi token trực tiếp trong code. Thay vào đó đặt biến môi trường:
- `TELEGRAM_TOKEN` = 8274924758:AAEejL6RfRWjT_HbEfMMRbHTbQuvOyBTPxc
- `CHAT_ID` = 6794824681
- (tùy chọn) `MESSAGE` = thông điệp (mặc định: 💵 Nhận Miễn Phí)
- (tùy chọn) `MIN_DELAY` = số giây nhỏ nhất giữa 2 lần gửi (mặc định 600)
- (tùy chọn) `MAX_DELAY` = số giây lớn nhất giữa 2 lần gửi (mặc định 900)

## Chạy cục bộ (Linux/macOS)
```bash
export TELEGRAM_TOKEN="8274924758:AAEejL6RfRWjT_HbEfMMRbHTbQuvOyBTPxc"
export CHAT_ID="6794824681"
export MESSAGE="💵 Nhận Miễn Phí"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bot.py