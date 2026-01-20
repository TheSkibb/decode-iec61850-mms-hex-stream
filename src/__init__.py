"""
compiles the mms asn and exposes the mms object
"""

import asn1tools

asn1_text = ""

with open("./mms.asn") as f:
    asn1_text = f.read()

    # Compile ASN.1 (BER)
mms = asn1tools.compile_string(asn1_text, 'ber')
