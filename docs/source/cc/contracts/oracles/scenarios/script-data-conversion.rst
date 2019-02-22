**************************
Script for a type S Oracle
**************************

The following script converts data entered in normal text form to a format acceptable by an Oracle of type: ``S`` that has the first two bytes as the length in **Little Endian** format and the rest of the data follows it. 

.. code-block:: python

    #!/usr/bin/env python3
    import sys
    import codecs
    import time
    import readline


    while True:
        message = input("Type message: ")
        #convert message to hex
        rawhex = codecs.encode(message).hex()

        #get length in bytes of hex in decimal
        bytelen = int(len(rawhex) / int(2))
        hexlen = format(bytelen, 'x')

        #get length in big endian hex
        if bytelen < 16:
            bigend = "000" + str(hexlen)
        elif bytelen < 256:
            bigend = "00" + str(hexlen)
        elif bytelen < 4096:
            bigend = "0" + str(hexlen)
        elif bytelen < 65536:
            bigend = str(hexlen)
        else:
            print("message too large, must be less than 65536 characters")
            continue

        #convert big endian length to little endian, append rawhex to little endian length
        lilend = bigend[2] + bigend[3] + bigend[0] + bigend[1]
        fullhex = lilend + rawhex

        print(fullhex)
