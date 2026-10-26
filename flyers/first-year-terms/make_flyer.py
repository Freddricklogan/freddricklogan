"""Build the first-year Elevate terms-and-conditions flyer.

Usage: python3 make_flyer.py "https://signing-link"
Writes qr.png, flyer.html; render with render.js.
"""
import sys
import segno
from PIL import Image

URL = sys.argv[1] if len(sys.argv) > 1 else "https://elevate.iit.edu/"
SCARLET = "#C8102E"

qr = segno.make(URL, error="h")
qr.save("qr_raw.png", scale=24, border=2, dark=SCARLET, light="#ffffff")

code = Image.open("qr_raw.png").convert("RGBA")
mark = Image.open("logo-red-white.png").convert("RGBA").crop((0, 0, 414, 414))
side = int(code.width * 0.22)
mark = mark.resize((side, side), Image.LANCZOS)
pad = int(side * 0.12)
backing = Image.new("RGBA", (side + 2 * pad, side + 2 * pad), "white")
backing.paste(mark, (pad, pad), mark)
pos = ((code.width - backing.width) // 2, (code.height - backing.height) // 2)
code.paste(backing, pos)
code.convert("RGB").save("qr.png")

display_url = URL.replace("https://", "").replace("http://", "").rstrip("/")
html = open("flyer_template.html").read().replace("{{URL}}", display_url)
open("flyer.html", "w").write(html)
print("QR encodes:", URL)
