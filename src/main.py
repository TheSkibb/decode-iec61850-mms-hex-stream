# Requires: pip install asn1tools
import binascii
import sys
from src import mms

if len(sys.argv) < 2:
    print("please supply a hex stream")

hex_stream = sys.argv[1]

# Replace this with any MMS BER hex payload you want to decode (MmsPdu bytes only)
# Example: the GetNameList sample you posted earlier
# bytes for: confirmedRequestPdu invokeID=1 getNameList ...
data = binascii.unhexlify(hex_stream)

# Decode top-level
decoded = mms.decode('MmsPdu', data)

# If you want to pretty-print nested results:
print(decoded)
