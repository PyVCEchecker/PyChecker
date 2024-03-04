from PIL import Image

im = Image.open("../imgs/space.jpeg")
im.load()
print("Size: {}x{}".format(*im.size))

out_size = (320, 213)

im.resize(out_size, Image.BICUBIC, reducing_gap=None).save("_bic.ref.png")
for reducing_gap in range(1, 4):
    im.resize(out_size, Image.BICUBIC, reducing_gap=reducing_gap).save(
        f"_bic.{reducing_gap}.png"
    )

im.resize(out_size, Image.LANCZOS, reducing_gap=None).save("_lzs.ref.png")
for reducing_gap in range(1, 4):
    im.resize(out_size, Image.LANCZOS, reducing_gap=reducing_gap).save(
        f"_lzs.{reducing_gap}.png"
    )
