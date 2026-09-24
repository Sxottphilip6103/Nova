from PIL import Image

SRC = "/home/claude/inspect/Nova_upload/icon/Novaicon-250.png"
BG = (5, 7, 16, 255)  # app's --bg, matches the icon's own dark background

master = Image.open(SRC).convert("RGBA")

def save_any(size, path):
    im = master.resize((size, size), Image.LANCZOS)
    im.save(path, "PNG")

def save_maskable(size, path, safe_scale=0.8):
    canvas = Image.new("RGBA", (size, size), BG)
    inner = int(size * safe_scale)
    art = master.resize((inner, inner), Image.LANCZOS)
    offset = (size - inner) // 2
    canvas.paste(art, (offset, offset), art)
    canvas.save(path, "PNG")

save_any(192, "icons/icon-192.png")
save_any(512, "icons/icon-512.png")
save_maskable(192, "icons/icon-maskable-192.png")
save_maskable(512, "icons/icon-maskable-512.png")

# apple touch icon: opaque, full-bleed square, no alpha
apple = master.resize((180, 180), Image.LANCZOS).convert("RGB")
apple.save("icons/apple-touch-icon.png", "PNG")

print("done")
