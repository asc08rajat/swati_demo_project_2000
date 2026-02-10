def search(q):
    if q == "timeout":
        raise TimeoutError("SearchTimeout")
    if q == "empty":
        raise LookupError("NoResults")
