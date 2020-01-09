# in this Script we use our DataFrame Class to compare de Energy production from 2 years
# for that we should provride 2 file name as argument (f1 and f2) in the command line
# the both files shouls be csv files


import argparse             # we import argparse modul. it allow us to use argument in command line
from DataFrame import DataFrame

if __name__ == '__main__': 
    # we first initilise our two arguments
    parser = argparse.ArgumentParser(description='zu ueberpruefende Users')
    parser.add_argument('-f1', '--file1', type=str, default='', help='first File')
    parser.add_argument('-f2', '--file2', type=str, default='', help='second File')
    args = parser.parse_args()

    #check if the two files were provided, if yes we make our calculations and plot the result.
    if args.file1 and args.file2:
        data_frame = DataFrame(args.file1, args.file2)
        data_frame.berechne_anteil_wind()
        data_frame.save_als_xlsx()
        data_frame.plot()
    else:
        # if not we just print we just print a message please provides two files
        print("please provide two file")