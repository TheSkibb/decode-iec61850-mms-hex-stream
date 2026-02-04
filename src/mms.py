def parse(input: bytes):
    try:
        decoded = mms.decode('MmsPdu', input)
    except Exception as e:
        print("could not decode object", e)
        return None
    return decoded
    
def encode(input):
    try:
        encoded = mms.encode('MmsPdu', input)
    except Exception as e:
        print("could not encode object", e)
        return None
    return encoded
