from functools import partial
from timeit import repeat

from PIL import Image


def run_tests(name, stmt):
    print()
    print(name)
    print("=" * len(name))
    print("   ", "".join(f"{x:>6}" for x in range(1, 16)))

    for yscale in range(1, 16):
        print(f"{yscale:>3}:", end="")
        for xscale in range(1, 16):
            to_run = partial(stmt, xscale, yscale)
            runs = sorted(repeat(to_run, number=1, repeat=7))
            median_ms = sum(runs[2:-2]) / (len(runs) - 4) * 1000
            print(f" {f'{median_ms:5.1f}':>5}", end="")
        print()


im = Image.open("../imgs/space.jpeg")
im.load()
print("Size: {}x{}".format(*im.size))


def reduce(xscale, yscale):
    return im.reduce((xscale, yscale))


def box_resize(xscale, yscale):
    size = (im.width // xscale, im.height // yscale)
    return im.resize(size, Image.BOX, (0, 0, size[0] * xscale, size[1] * yscale))


run_tests("Reduce", reduce)
# run_tests("BOX resize", box_resize)
