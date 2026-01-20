def parse(input: bytes):
    try:
        decoded = mms.decode('MmsPdu', data)
    except Exception as e:
        print("could not decode object", e)
        return None
    return decoded
    
