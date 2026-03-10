# decode IEC61850 mms hex streams into python objects

small tool for my thesis

## Usage

~~~
./run.sh <hex stream>
~~~

you can get the hex stream from wireshark, or from another sniffer

you can also import the compiles mms with

The `-e` flag lets you encode a mms object back into a byte array

~~~
python -m src.main -e <mms object>
~~~

~~~
from src import mms
~~~

## Example

~~~
./run.sh a020020102a11ba003800100a114811253545241544f4e5f4945444c446576696365
~~~

~~~
('confirmedRequestPdu', {'invokeID': 2, 'confirmedServiceRequest': ('getNameList', {'objectClass': ('basicObjectClass', 0), 'objectScope': ('domainSpecific', 'STRATON_IEDLDevice')})})
~~~

## Using as library

you can also use this as a module in your python scripts by cloning the repo and using it as a module

~~~py
from src import parse, mms

decoded = parse(b'<some byte array of mms request')

encoded = mms.encode(decoded)
~~~

## some known errors

cant parse conclude-Request/ResponsePDU (8b00 and 8c00)
