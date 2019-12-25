# Bkfile
Backup the code source of webs
## Installing
Install and update using pip:  
``
pip install requests
pip install retrying
``

## A Simple Example
* Upload bk.php to your webroot
* Run bkfile.py  
``
python3 bkfile.py -u "http://domain/bk.php" -p "/var/wwwroot/html"
``

