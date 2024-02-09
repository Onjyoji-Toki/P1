#!/usr/bin/env python3
import time
import sys
from dS3484.relay import RelayStatus, dS3484
from wavedump import wavedump
from pas2018.ramp_up import ramp_up
from pas2018.ramp_down import ramp_down
from rename.rename import rename_down, rename_up, make_file
from mcp9600.temp import temp, TEE
from temp_mail import temp_mail
from relay_mail import relay_mail

def main():
    now = time.localtime()
    start_time = time.strftime('%m%d%H%M', now)
    make_file(start_time)
    
    def try_off(ch, on_off):
        for i in range(10):
            try:
                ds_dev.set_relay(ch, on_off)
            except Exception as err:
                print(err)
                print(f'Retry: {i}')
                time.sleep(10)
            else:
                time.sleep(0.1)
                return

        relay_mail()
        raise Exception('Cannot connect to relay.')
        
    try:
        for loop in range(1):   #Edit here to change the number of loop
            ds_dev = dS3484('192.168.0.123', 17123)  #Edit here!! Please write IP address for dS3484
            print(ds_dev.get_status())
            try_off(1, RelayStatus.on)
            try_off(2, RelayStatus.on)
            try_off(3, RelayStatus.off)
            try_off(4, RelayStatus.off)
            print(ds_dev.get_relays()[:8])
            print(ds_dev.get_analog())
            print(ds_dev.get_inputs())
        
            ramp_up()

            time.sleep(2) 
            wavedump()
            time.sleep(2)

            ramp_down()
            
            temp()

            print(ds_dev.get_status())
            try_off(1, RelayStatus.off)
            try_off(2, RelayStatus.off)
            try_off(3, RelayStatus.off)
            try_off(4, RelayStatus.off)
            print(ds_dev.get_relays()[:8])
            print(ds_dev.get_analog())
            print(ds_dev.get_inputs())
    
            rename_down(loop,start_time)
            time.sleep(2) 

            print(ds_dev.get_status())
            try_off(1, RelayStatus.off)
            try_off(2, RelayStatus.off)
            try_off(3, RelayStatus.on)
            try_off(4, RelayStatus.on)
            print(ds_dev.get_relays()[:8])
            print(ds_dev.get_analog())
            print(ds_dev.get_inputs())
            
            ramp_up()

            time.sleep(2) 
            wavedump()
            time.sleep(2) 
            
            ramp_down()

            temp()

            print(ds_dev.get_status())
            try_off(1, RelayStatus.off)
            try_off(2, RelayStatus.off)
            try_off(3, RelayStatus.off)
            try_off(4, RelayStatus.off)
            print(ds_dev.get_relays()[:8])
            print(ds_dev.get_analog())
            print(ds_dev.get_inputs())

            rename_up(loop,start_time)
            time.sleep(2)
            
            
    except TEE as e:
        print(f"temperture exceeded 100 degree celsius: {e}")
        temp_mail()
        print(ds_dev.get_status())
        try_off(1, RelayStatus.off)
        try_off(2, RelayStatus.off)
        try_off(3, RelayStatus.off)
        try_off(4, RelayStatus.off)
        print(ds_dev.get_relays()[:8])
        print(ds_dev.get_analog())
        print(ds_dev.get_inputs())
        sys.exit()

if __name__ == '__main__':
    main()
