import datetime

def main():    
    dt_now = datetime.datetime.now()
    start_time = dt_now.strftime('%Y%m%d%H%M%S')
    print(start_time)
    print(type(start_time))

if __name__ == '__main__':
    main()    