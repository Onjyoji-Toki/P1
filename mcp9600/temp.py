import board
import busio
import adafruit_mcp9600
import time
import os

os.environ["BLINKA_MCP2221"] = "1"

class TEE(Exception):
    pass

def temp():
    '''Main function.'''
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    mcp = adafruit_mcp9600.MCP9600(i2c, address=103)

    print((mcp.ambient_temperature, mcp.temperature, mcp.delta_temperature))
    f = open('temp.txt', 'a')
    f.write(str(mcp.temperature) + '\r\n')
    f.close()
    if mcp.temperature > 100:
        raise TEE("temperture exceeded 100 degree celsius")
    time.sleep(1)