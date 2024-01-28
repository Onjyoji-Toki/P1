#!/usr/bin/env python3
from current_controller import CurrentController

def main():
    '''Ramp up.'''
    c_con = CurrentController()
    c_con.ramp_from_to(6, 0, wait=0.2)

if __name__ == '__main__':
    main()
