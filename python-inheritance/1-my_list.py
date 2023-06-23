#!/usr/bin/python3
'''
My list module
'''


class MyList(list):
    '''
    Inherits class from list
    '''
    def print_sorted(self):
        '''
        print sorted list
        '''
        print(sorted(self))
