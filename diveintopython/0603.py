f = open("/music/_singles/kairo.mp3", "rb")
f
f.mode
f.name

f.tell()
f.seek(-128, 2)
f.tell
tagData = f.read(128)
tagData
f.tell