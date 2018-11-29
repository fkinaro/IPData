# IPData
* Simple Python script to get details about a hostname or IP address
* This project is inspired by [This article](https://null-byte.wonderhowto.com/how-to/hack-like-pro-find-exact-location-any-ip-address-0161964/) on [null-byte](https://null-byte.wonderhowto.com)
* You can use:
    - IPv4 Addresses
    - IPv6 Addresses
    - Hostnames
## Dependencies
1. [pygeoip](https://pypi.org/project/pygeoip/ "pygeoip project page")
2. [Virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/ "Installing virtualenv")

## Install instructions
1. Clone the repo: `git clone https://github.com/fkinaro/IPData.git`
2. Run `python3 -m virtualenv IPData`
3. Change to the project directory: `cd IPData`
4. Download the database `wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz`
5. Decompress the archive: `gzip -d GeoLiteCity.dat.gz`
6. Run `source bin/activate` to activate your virtual environment.
7. Set the script as executable: `chmod +x app.py`
8. Execute the script: `./app.py`
