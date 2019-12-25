# Bkfile
Backup the code source of webs
## Installing
Install and update using pip:
``
pip install requests
pip install retrying
``

## A Simple Example
1.Upload bk.php to your webroot
2.
``
python3 bkfile.py -u "http://domain/bk.php" -p "/var/wwwroot/html"
``

