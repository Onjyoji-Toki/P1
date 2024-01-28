#!/usr/bin/env python3
import os
from argparse import ArgumentParser

os.environ["BLINKA_MCP2221"] = "1"
import board
import busio


class DAC:
    def __init__(self):
        self._dev = busio.I2C(board.SCL, board.SDA)
        self._addr = 95

    def _write(self, command, data):
        self._dev.writeto(self._addr, bytearray([command] + data))

    def set_voltage(self, voltage, channel=0):
        '''Set voltage. 
        
        Parameters
        ----------
        voltage : float
            Voltage to output.
        channel : int, optional
            Channel to set voltage (0 or 1). Default to 0.
        '''
        assert 0 <= voltage <= 10
        assert channel in [0, 1]

        code = list((int((voltage/10)*0xfff) << 4).to_bytes(2, 'little'))
        self._write(0x02 << channel, code)

def main():
    '''Main function.'''
    parser = ArgumentParser()
    parser.add_argument('voltage', help='DAC output voltage.', type=float)
    args = parser.parse_args()

    dac = DAC()
    dac.set_voltage(args.voltage)
    

if __name__ == '__main__':
    main()
