**SQM Finder**

This little script shall help to find your Sky Quality Meter (SQM) on the network.

_How it works_

According to Unihedron's manual, the SQM's Lantronic XPort will respond to the hex string 00 00 00 F6 received at UDP port 30718.
The Lantronix XPort will send a response that starts with hex 00 00 00 F7 (elements 1-4), and elements 25-30 contain the MAC address of the responding unit.

Enjoy!
