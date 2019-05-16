# CIS DIGIKEY IMPORTER
This is an automatic components importer from Digi-Key to CIS.

## INSTRUCTIONS:

### CIS database setup
Create a local CIS Microsoft Access based database. look at my_orcad_cis_db.ldb as an example format.
instructions on how to create a local database can be found on https://www.youtube.com/watch?v=qTzcHqxomOE


### Configuring database settings in the app
open add_component.py and change the following lines to your database settings:
```
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb)};'
    r'DBQ=D:\CIS_DB\my_orcad_cis_db.MDB;'
    )
```
### Importing components from digikey
**note: this application has been tested only on Chrome browser**
1) go to a desired component page (ex: https://www.digikey.com/product-detail/en/on-semiconductor/LM317LDR2G/LM317LDR2GOSTR-ND/918503)
2) select the entire page (CTRL + a) and copy. 
3) open add_component.py and follow the instructions.
