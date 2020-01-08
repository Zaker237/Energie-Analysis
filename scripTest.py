import argparse
from DataFrame import DataFrame

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='zu ueberpruefende Users')
    parser.add_argument('-f1', '--file1', type=str, default='', help='first File')
    parser.add_argument('-f2', '--file2', type=str, default='', help='second File')
    args = parser.parse_args()
    print("debut-----------------------------------------------------------------------")
    if args.file1 and args.file2:
        data_frame = DataFrame(args.file1, args.file2)
        data_frame.berechne_anteil_wind()
        data_frame.save_als_xlsx()
        data_frame.plot()
    else:
        print("provide two file")