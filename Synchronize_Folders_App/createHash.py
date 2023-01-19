import hashlib

def sha1(filename):
    BUF_SIZE = 1  # read in specified ammounts so we can deal with big files faster
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()