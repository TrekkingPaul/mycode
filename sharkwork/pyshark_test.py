#!/usr/bin/python3
"""Testing pyshark module"""

#pip install -m pyshark
import pyshark

capture = pyshark.LiveCapture(interface='docker0')
capture.sniff(timeout=30)

capture


