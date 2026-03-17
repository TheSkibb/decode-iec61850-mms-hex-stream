import binascii
from src import mms

b = binascii.unhexlify("0300004c02f08001000100613f303d020103a038a03602020181a430800100a12ba0293027a025a1231a0d414131443151303151315141311a12584342523124535424506f7324737456616c")

mmsStart = 20

print(mms.decode("MmsPdu", b[mmsStart:]))

def changeInvokeID(b: bytes, newInvokeID: int) -> bytes:
    offset = 3 # offset from mms start to length tag
    numBytes = b[mmsStart+offset]
    invokeIDStart = mmsStart+offset+1
    invokeIDEnd = mmsStart+offset+1+numBytes
    print(f"getting values from {invokeIDStart} to {invokeIDEnd}")
    oldValue = b[invokeIDStart:invokeIDEnd]
    len(oldValue)
    print(int.from_bytes(oldValue, byteorder="big", signed=True))

    b = bytearray(b) #convert the bytes object so we can modify it
    b[invokeIDStart:invokeIDEnd] = newInvokeID.to_bytes(2, signed=True)
    b = bytes(b)

    return b

b = changeInvokeID(b, 1)
print(mms.decode("MmsPdu", b[mmsStart:]))
