# decode IEC61850 mms hex streams into python objects

small tool for my thesis

## Usage

~~~
./run.sh <hex stream>
~~~

you can get the hex stream from wireshark, or from another sniffer

you can also import the compiles mms with

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
