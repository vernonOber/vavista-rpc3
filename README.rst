vavista_rpc (Python access to VistA RPCs)
=========================================

The vavista_rpc.brokerRPC3 module provides a very simple mechanism for calling VistA RPCs.
Simply connect, and call the RPC you are interested in.

The vavista.rpc module does not depend on the M interfaces modules, i.e.
it is not bound to a GT.M interpreter. It communicates client server over
a TCP connection.

brokerRPC3.py has been modified to work with Python 3. Running from the
command line will enter an interactive testing session with the
context "XUPROGMODE".

Credit
------

The brokerRPC.py code belongs to Caregraph.org's FMQL product. Forked
from https://github.com/kevingill1966/vavista-rpc 1/2020 .

The brokerRPC3.py code is a modification to run under
Python 3. I do not yet understand all of the technical details
of the VistA RPC Broker to vouch for the documentation
listed here, or the completeness. -Vernon Oberholzer 2/2020

Setup Information
-----------------
Ideally first setup a Python 3 virtual env.
 1. mkdir vavista
 2. cd vavista
 3. python3 -m venv venv
 4. source venv/bin/activate
 5. download the dist dir
 6. pip install dist/vavista_rpc-0.0.9-py3-none-any.whl
 7. Or, just download and use the module vavista_rpc/brokerRPC3.py directly


**Application Context**

In order to access RPCs in Vista, you need to have a valid Application Context Id. 

The application context provides the security management for RPCs. The context must
exist in the table "OPTION" (19), with the Type = "Broker (client/server)" (B). 


**RPC Port**

VistA provides a RPC (remote procedure call) broker. This sits on an agreed port.

Clients connect to the broker and create a session. In the GT.M context, a server
is forked to process the request. The server waits, receives a request, processes
it and returns a response. The mechanism is single-threaded and synchronous.

9210 - where is this configured ?? TODO RPC BROKER SITE PARAMETERS seems do describe
other sites configurations, not this sites.

**How individual Requests are Configured in Vista**

The available RPCs are listed in Fileman file "REMOTE PROCEDURE" (8994).

TODO: rpc availability what is public??

The RPC may be restricted to one application. TODO: how???

How to set up package: TODO

The Option allows you to assign restricted RPCs to the application context.

All results from RPCs are returned as a single string.
RPCs have the following return types::

       1        SINGLE VALUE (string)
       2        ARRAY (string split by \r\n)
       3        WORD PROCESSING (string split by \r\n)
       4        GLOBAL ARRAY (string split by \r\n)
       5        GLOBAL INSTANCE (string)

Parameters can be::

       1        LITERAL - PLiteral
       2        LIST - PList
       2        Word Processing - PLiteral
       4        REFERENCE - PReference

connect
-------

Create a connection::

    from vavista import rpc, PLiteral, PList, PReference
    c = rpc.connect(hostname, port, access-code, verify-code, context, debug=False)

        - TCP communication information (hostname, port)
        - VistA's security (access, verify)
        - application context - See note above
        - the debug flag is useful for interactive use.

This function creates a connection to the VISTA RPC server.


Example Code
------------
python -m vavista_rpc.brokerRPC3 <host> <port> <access> <verify>
 (enters and interactive testing session)

Study the main_test() function in brokerRPC3 for an example how to execute an RPC

References
----------

 - XWBPRS.m

 - http://www.caregraf.org

 - http://www.va.gov/vdl/application.asp?appid=23
