

# listcomp
# generates all in one go.

# symbol = '$@#'
# codes = [ord(sym) for sym in symbol]
# print(codes)

colors = 'black white'.split()
size = 'S M L'.split()
tshirts = [(c, s) for c in colors for s in size]
print(tshirts)
