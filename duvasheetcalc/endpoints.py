from duvasheetcalc.sheetloader import SheetLoader
import argparse


parser = argparse.ArgumentParser()

def calc_sheet():
    parser.add_argument('--file')
    parser.add_argument('--out')
    args = parser.parse_args()

    loader = SheetLoader()
    ok = loader.load(args.file, args.out)

    if ok:
        print('Done {}'.format(args.out))
    else:
        print('Something went wrong.')
