import sys, os, hashlib

def convert_list_to_hash(some_stupid_list):
    hashes = {}
    for element in some_stupid_list:
        bytepiece = bytes(element, "utf-8")
        readable_hash = hashlib.sha256(bytepiece).hexdigest()
        hashes[element] = readable_hash
    return hashes