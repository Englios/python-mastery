'''
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 10
'''

import csv
import sys
import os


def portfolio_cost(filename):
    with open (filename,'r') as f:
        totalsum=0
        for line in f:
            fields = line.split()
            try:
                nshare=int(fields[1])
                price=float(fields[2])
                share_price=nshare*price
                print(f'{fields[0]:<10s}{nshare:>10d}{price:>10.2f}{share_price:>10.2f}')
                totalsum+=share_price
                
            except ValueError as e:
                print('\nBad line',line,end='')
                print('Reason',e,end='\n\n')
                continue
    print('-'*50)       
    print('\nTotal sum of all prices',round(float(totalsum),2),end='\n\n')
    return round(totalsum,2)
    
        

        