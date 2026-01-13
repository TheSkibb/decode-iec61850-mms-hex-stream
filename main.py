# Requires: pip install asn1tools
import pprint
import asn1tools
import binascii
import textwrap
import os
import sys

if len(sys.argv) < 2:
    print("Error please supply a hex stream")
    sys.exit()

hex_stream = sys.argv[1]

asn1_text = ""

with open("./mms.asn") as f:
    asn1_text = f.read()

    # Compile ASN.1 (BER)
mms = asn1tools.compile_string(asn1_text, 'ber')

# Replace this with any MMS BER hex payload you want to decode (MmsPdu bytes only)
# Example: the GetNameList sample you posted earlier
# bytes for: confirmedRequestPdu invokeID=1 getNameList ...
data = binascii.unhexlify(hex_stream)

# Decode top-level
decoded = mms.decode('MmsPdu', data)

# If you want to pretty-print nested results:
print(decoded)
