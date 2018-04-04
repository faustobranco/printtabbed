# Print Tabbed

Class with functions to format list of dicts on table 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Developed and tested in Linux Ubuntu and Python 2.7


### Installing

A step by step series of examples that tell you have to get a development env running

1. Create a folder called "print_tabbed.py" inside the folder of your project.
2. Copy the print_tabbed.py.py and `__init__.py` files to the print_tabbed.py folder
3. Do class import for your project normally.

* If the import is successful, a file called print_tabbed.py.pyc must be created, this file (compiled python file) must be maintained.

## Functions

### print_tabbed

print_tabbed(lst_Tabbed, header=False, fprint=True):
        """
        Desc: print_tabbed: 

Description: Print or Return a formated table of list of dict, with columns, headers, etc

**lst_Tabbed**: list of dict to formant
**header**: print headers?
**fprint**: fprint = True: Print on screen; fprint = False: Return formated lines in a list

The list of dict to be formated must be in the format:
[{'Title1': 'Value', 'Title2': 'Value', 'Title3': 'Value', 'Title4': 'Value', ...},
 {'Title1': 'Value2', 'Title2': 'Value2', 'Title3': 'Value2', 'Title4': 'Value2', ...},
 ...]
 Or
[{'Title1': 'Value', 'Title2': 'Value', 'Title3': 'Value', 'Title4': [{SubTile1}], ...},
 {'Title1': 'Value2', 'Title2': 'Value2', 'Title3': 'Value2', 'Title4': 'Value2', ...},
 ...]
    
Return: List of each line (formated) Or None if set to print
              
## Deployment

Additional notes about how to deploy this on a live system:
Para deploy em ambiente de live:
1) Create a folder called "print_tabbed" inside the folder of your project.
2) Copy the print_tabbed.pyc and `__init__.pyc` files to the print_tabbed folder

Note: Unless you really have experience, do not install directly on /usr/local/lib/python2.7/dist-packages

For next versions will be available installation by setup or pip.

## Examples of use

```
lst_Teste2 = [{'IP': '12.209.29.4', 'Link': False, 'Exists': False, 'Path': '/mnt/heapdump'},
{'IP': '12.209.29.4', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/saved_caches'},
{'IP': '12.209.29.4', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/hint'},
{'IP': '12.209.29.4', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/commitlog'},
{'IP': '12.209.29.5', 'Link': False, 'Exists': False, 'Path': '/mnt/heapdump'},
{'IP': '12.209.29.5', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/saved_caches'},
{'IP': '12.209.29.5', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/hint'},
{'IP': '12.209.29.5', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/commitlog'},
{'IP': '12.209.29.6', 'Link': False, 'Exists': False, 'Path': '/mnt/heapdump'},
{'IP': '12.209.29.6', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/saved_caches'},
{'IP': '12.209.29.6', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/hint'},
{'IP': '12.209.29.6', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/commitlog'},
{'IP': '12.209.30.68', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/saved_caches'},
{'IP': '12.209.30.68', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/hint'},
{'IP': '12.209.30.68', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/commitlog'},
{'IP': '12.209.30.69', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/saved_caches'},
{'IP': '12.209.30.69', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/hint'},
{'IP': '12.209.30.69', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/commitlog'},
{'IP': '12.209.30.70', 'Link': False, 'Exists': False, 'Path': '/mnt/heapdump'},
{'IP': '12.209.30.70', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/saved_caches'},
{'IP': '12.209.30.70', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/hint'},
{'IP': '12.209.30.70', 'Link': False, 'Exists': False, 'Path': '/mnt/cassandra/commitlog'}]

lst_Teste3 =[{'IP': '12.209.29.4', 'Options': [{'Recommended': False, 'Used': True, 'Setting': 'incremental_backups'}, {'Recommended': '/mnt/cassandra/saved_caches', 'Used': '/logsdrive/cassandra/saved_caches', 'Setting': 'saved_caches_directory'}, {'Recommended': False, 'Used': True, 'Setting': 'auto_snapshot'}, {'Recommended': '/mnt/cassandra/hints', 'Used': '/logsdrive/cassandra/hints', 'Setting': 'hints_directory'}, {'Recommended': '/mnt/cassandra/commitlog', 'Used': '/mnt/cassandra/logs', 'Setting': 'commitlog_directory'}]},
{'IP': '12.209.29.5', 'Options': [{'Recommended': False, 'Used': True, 'Setting': 'incremental_backups'}, {'Recommended': '/mnt/cassandra/saved_caches', 'Used': '/logsdrive/cassandra/saved_caches', 'Setting': 'saved_caches_directory'}, {'Recommended': False, 'Used': True, 'Setting': 'auto_snapshot'}, {'Recommended': '/mnt/cassandra/hints', 'Used': '/logsdrive/cassandra/hints', 'Setting': 'hints_directory'}, {'Recommended': '/mnt/cassandra/commitlog', 'Used': '/mnt/cassandra/logs', 'Setting': 'commitlog_directory'}]},
{'IP': '12.209.29.6', 'Options': [{'Recommended': False, 'Used': True, 'Setting': 'incremental_backups'}, {'Recommended': '/mnt/cassandra/saved_caches', 'Used': '/logsdrive/cassandra/saved_caches', 'Setting': 'saved_caches_directory'}, {'Recommended': False, 'Used': True, 'Setting': 'auto_snapshot'}, {'Recommended': '/mnt/cassandra/hints', 'Used': '/logsdrive/cassandra/hints', 'Setting': 'hints_directory'}, {'Recommended': '/mnt/cassandra/commitlog', 'Used': '/mnt/cassandra/logs', 'Setting': 'commitlog_directory'}]},
{'IP': '12.209.30.68', 'Options': [{'Recommended': False, 'Used': True, 'Setting': 'auto_bootstrap'}, {'Recommended': False, 'Used': True, 'Setting': 'incremental_backups'}, {'Recommended': '/mnt/cassandra/saved_caches', 'Used': '/logsdrive/cassandra/saved_caches', 'Setting': 'saved_caches_directory'}, {'Recommended': False, 'Used': True, 'Setting': 'auto_snapshot'}, {'Recommended': '/mnt/cassandra/hints', 'Used': '/logsdrive/cassandra/hints', 'Setting': 'hints_directory'}, {'Recommended': '/mnt/cassandra/commitlog', 'Used': '/mnt/cassandra/logs', 'Setting': 'commitlog_directory'}]},
{'IP': '12.209.30.69', 'Options': [{'Recommended': False, 'Used': True, 'Setting': 'auto_bootstrap'}, {'Recommended': False, 'Used': True, 'Setting': 'incremental_backups'}, {'Recommended': '/mnt/cassandra/saved_caches', 'Used': '/logsdrive/cassandra/saved_caches', 'Setting': 'saved_caches_directory'}, {'Recommended': False, 'Used': True, 'Setting': 'auto_snapshot'}, {'Recommended': '/mnt/cassandra/hints', 'Used': '/logsdrive/cassandra/hints', 'Setting': 'hints_directory'}, {'Recommended': '/mnt/cassandra/commitlog', 'Used': '/mnt/cassandra/logs', 'Setting': 'commitlog_directory'}]},
{'IP': '12.209.30.70', 'Options': [{'Recommended': False, 'Used': True, 'Setting': 'auto_bootstrap'}, {'Recommended': False, 'Used': True, 'Setting': 'incremental_backups'}, {'Recommended': '/mnt/cassandra/saved_caches', 'Used': '/logsdrive/cassandra/saved_caches', 'Setting': 'saved_caches_directory'}, {'Recommended': False, 'Used': True, 'Setting': 'auto_snapshot'}, {'Recommended': '/mnt/cassandra/hints', 'Used': '/logsdrive/cassandra/hints', 'Setting': 'hints_directory'}, {'Recommended': '/mnt/cassandra/commitlog', 'Used': '/mnt/cassandra/logs', 'Setting': 'commitlog_directory'}]}]


import printtabbed

objPrint = printtabbed.print_tabbed()

objPrint.print_tabbed(lst_Teste2, True)
        
objPrint.print_tabbed(lst_Teste3, True)
objPrint.print_tabbed(lst_Teste3[0]['Options'], True)


lst_Retorno = objPrint.print_tabbed(lst_Teste2, True, fprint=False)

for linha in lst_Retorno:
    print linha
    
```
[![](https://github.com/faustobranco/printtabbed/blob/master/Capture.PNG)](https://github.com/faustobranco/printtabbed/blob/master/Capture.PNG)
[![](https://github.com/faustobranco/printtabbed/blob/master/Capture2.PNG)](https://github.com/faustobranco/printtabbed/blob/master/Capture2.PNG)

## Versioning
```
=======================================================================================
== Log Changes:
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================
```
## Authors
```
=======================================================================================
== Script Info:		print_tabbed.py - Class with functions to format list of dicts on table 
==
=======================================================================================
== Create Author:	Fausto Branco
== Create Date:		2018-04-03
== Actual Version:  1.0.0
== Description:		
=======================================================================================
== Log Changes:
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================
```
## License



