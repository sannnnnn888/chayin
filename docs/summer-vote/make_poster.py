"""夏日消暑饮品海报 - QR码合成"""
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

POSTER_PATH = r"C:\Users\san\Desktop\CC资料\tea-survey\docs\summer-vote\poster_raw.png"
OUTPUT_PATH = r"C:\Users\san\Desktop\CC资料\夏日消暑饮品海报.png"
QR_URL = "https://sannnnnn888.github.io/chayin/summer-vote/"

# Load poster
poster = Image.open(POSTER_PATH).convert("RGBA")
pw, ph = poster.size
print(f"Poster size: {pw}x{ph}")

# Generate QR code
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=2,
)
qr.add_data(QR_URL)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="#2c3e50", back_color="white").convert("RGBA")

# Scale QR code - roughly 1/6 of poster width
qr_target_size = pw // 5  # ~230px on 1152px poster
qr_img = qr_img.resize((qr_target_size, qr_target_size), Image.LANCZOS)
print(f"QR size: {qr_target_size}x{qr_target_size}")

# Create a white rounded background for QR code
padding = 20
bg_size = qr_target_size + padding * 2
bg = Image.new("RGBA", (bg_size, bg_size), (255, 255, 255, 220))

# Draw rounded rectangle background
draw = ImageDraw.Draw(bg)
draw.rounded_rectangle(
    [(0, 0), (bg_size - 1, bg_size - 1)],
    radius=16,
    fill=(255, 255, 255, 230),
    outline=(255, 255, 255, 100),
    width=1,
)

# Position: bottom-right, with 40px margin
margin = 40
x = pw - bg_size - margin
y = ph - bg_size - margin

# Paste background
poster.paste(bg, (x, y), bg)

# Paste QR code on top of background
qr_x = x + padding
qr_y = y + padding
poster.paste(qr_img, (qr_x, qr_y), qr_img)

# Add "扫码投票" label below QR code
try:
    font = ImageFont.truetype("msyh.ttc", 28)  # Microsoft YaHei
except:
    font = ImageFont.load_default()

label = "扫码参与投票"
label_color = (44, 62, 80, 200)
draw_final = ImageDraw.Draw(poster)

# Get text size
bbox = draw_final.textbbox((0, 0), label, font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]

label_x = x + (bg_size - tw) // 2
label_y = y + bg_size + 8
# Draw label with shadow for readability
draw_final.text((label_x + 1, label_y + 1), label, font=font, fill=(255, 255, 255, 180))
draw_final.text((label_x, label_y), label, font=font, fill=label_color)

# Save
poster = poster.convert("RGB")
poster.save(OUTPUT_PATH, quality=95)
print(f"Poster saved: {OUTPUT_PATH}")
print(f"Final size: {poster.size}")
