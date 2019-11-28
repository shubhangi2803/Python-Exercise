import zlib
s="ShubhiAddy<3!ShubhiAddy<3!ShubhiAddy<3!ShubhiAddy<3!".encode()
t=zlib.compress(s)
print(t)
print(zlib.decompress(t))
