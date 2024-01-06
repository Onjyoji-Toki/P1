#!/usr/bin/env python3
import os
import time

os.environ["BLINKA_MCP2221"] = "1"
import board
import busio
import adafruit_mcp9600

def main():
    '''Main function.'''
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    mcp = adafruit_mcp9600.MCP9600(i2c, address=103)

    while True:
        print((mcp.ambient_temperature, mcp.temperature, mcp.delta_temperature))
        time.sleep(1)


if __name__ == '__main__':
    main()
