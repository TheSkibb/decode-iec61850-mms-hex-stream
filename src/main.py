# Requires: pip install asn1tools
import binascii
import sys
import ast

from src import mms


def decode(hex_stream):

    # Replace this with any MMS BER hex payload you want to decode (MmsPdu bytes only)
    # Example: the GetNameList sample you posted earlier
    # bytes for: confirmedRequestPdu invokeID=1 getNameList ...
    data = binascii.unhexlify(hex_stream)

    print(type(data))
    print(f"data before decoding {data}")
    # Decode top-level
    decoded = mms.decode('MmsPdu', data)

    # If you want to pretty-print nested results:
    print(decoded)

    print("re-encoding:")

    encode(decoded)

def encode(obj):
    # convert into an actual object
    obj = ast.literal_eval(obj)
    encoded = mms.encode('MmsPdu', obj)
    print(encoded)


if len(sys.argv) < 2:
    print("please supply a hex stream")

if sys.argv[1] == "-e":
    if len(sys.argv) < 3:
        print("usage: [-e] [mms object]")
    else:
        encode(sys.argv[2])
else: 
    decode(sys.argv[1])
