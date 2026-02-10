def play(v):
    if v == "age": raise PermissionError("AgeRestricted")
    if v == "network": raise ConnectionError("NetworkDown")
    if v == "format": raise TypeError("FormatError")
    if v == "codec": raise RuntimeError("CodecError")
