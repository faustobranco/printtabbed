#######################################################################################
## Script Info:		print_tabbed.py - Class with functions to format list of dicts on table 
##
#######################################################################################
## Create Author:	Fausto Branco
## Create Date:		2018-04-03
## Actual Version:  1.0.0
## Description:		
#######################################################################################
## Log Changes:
## Date:            2018-04-03
## Author:          Fausto Branco
## Version:         1.0.0
## Description:     Initial Version
#######################################################################################
import signal
import sys

__version__ = '1.0.0'

class print_tabbed:
    def print_tabbed(self, lst_Tabbed, header=False, fprint=True):
        """
        Desc: print_tabbed: Print or Return a formated table of list of dict, with columns, headers, etc
        The list to be formated must be in the format:
        [{'Title1': 'Value', 'Title2': 'Value', 'Title3': 'Value', 'Title4': 'Value', ...},
         {'Title1': 'Value2', 'Title2': 'Value2', 'Title3': 'Value2', 'Title4': 'Value2', ...},
         ...]
         Or
        [{'Title1': 'Value', 'Title2': 'Value', 'Title3': 'Value', 'Title4': [{SubTile1}], ...},
         {'Title1': 'Value2', 'Title2': 'Value2', 'Title3': 'Value2', 'Title4': 'Value2', ...},
         ...]
         
        """
        lst_Return = []
        lst_New_Tabbed = []
        for idx_item, type_item in enumerate([[type(value) for key, value in dct_lst_Items.items()] for dct_lst_Items in lst_Tabbed]):
            for idx_dict, type_dict in enumerate(type_item):
                if type_dict == list:
                   dct_Copy = lst_Tabbed[idx_item].copy()
                   lst_temp = []
                   lst_temp = self.print_tabbed(lst_Tabbed[idx_item].values()[idx_dict], True, False)
                   for item_lst_temp in lst_temp:
                       dct_Copy[lst_Tabbed[idx_item].keys()[idx_dict]] = item_lst_temp
                       lst_New_Tabbed.append(dict(dct_Copy))
        if len(lst_New_Tabbed) == 0:
           lst_New_Tabbed = lst_Tabbed[:]
        #Convert all items to string
        lst_Tabbed_tmp = [dict([a, str(x)] for a, x in b.items()) for b in lst_New_Tabbed]
        #Get len of all items and Key Names
        lst_length = [[max([len(item) for item in value.split('\n')]) for key, value in dct_lst_Items.items()] for dct_lst_Items in lst_Tabbed_tmp]
        lst_length = lst_length + [[len(key) for key, value in dct_lst_Items.items()] for dct_lst_Items in lst_Tabbed_tmp]
        #Get Max len of each item
        lst_Maxlength = [max(elem) for elem in zip(*lst_length)]
        #Prepare fmt sintax with max len
        str_fmt = ' '.join('{:<%d} | ' % l for l in lst_Maxlength)
        if header == True:
                if fprint == True:
                    print(str_fmt.format(*lst_Tabbed_tmp[0]))
                    print('-' * ((sum(lst_Maxlength) + len(lst_Maxlength) - 1) + (len(lst_Maxlength) * 3) - 1))  # separator
                else:
                    lst_Return.append(str_fmt.format(*lst_Tabbed_tmp[0]))
                    lst_Return.append('-' * ((sum(lst_Maxlength) + len(lst_Maxlength) - 1) + (len(lst_Maxlength) * 3) - 1))  # separator
        #Print all items with format
        for row in lst_Tabbed_tmp:
            if fprint == True:
                print(str_fmt.format(*row.values()))
            else:
                lst_Return.append(str_fmt.format(*row.values()))
        if fprint == False:
           return lst_Return

