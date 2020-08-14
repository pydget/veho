from veho.matrix.enumerate.zipper.zipper import zipper


def duozipper(ma, mb, fn):
    return zipper(ma, mb, fn)


def trizipper(ma, mb, mc, fn):
    zipped = list(zip(ma, mb, mc))
    for (i, (ra, rb, rc)) in enumerate(zipped):
        zipped[i] = (fn(a, b, c, i, j) for j, (a, b, c) in enumerate(zip(ra, rb, rc)))
    return zipped


def quazipper(ma, mb, mc, md, fn):
    zipped = list(zip(ma, mb, mc, md))
    for (i, (ra, rb, rc, rd)) in enumerate(zipped):
        zipped[i] = (fn(a, b, c, d, i, j) for j, (a, b, c, d) in enumerate(zip(ra, rb, rc, rd)))
    return zipped


def to_duozipper(fn):
    return lambda ma, mb: duozipper(ma, mb, fn)


def to_trizipper(fn):
    return lambda ma, mb, mc: trizipper(ma, mb, mc, fn)


def to_quazipper(fn):
    return lambda ma, mb, mc, md: quazipper(ma, mb, mc, md, fn)
