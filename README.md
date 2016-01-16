# openmediavault-monitoring-odroid-xu4
Some additional RRDTool graphs for OpenMediaVault Monitoring for your ODROID-XU4.
Should work for ODROID-XU3 as well.

## Installation
```Shell
wget https://github.com/Obihoernchen/openmediavault-monitoring-odroid-xu4/archive/master.zip
unzip master.zip
cd openmediavault-monitoring-odroid-xu4-master
cp -R usr/* /usr
cp -R var/* /var
rm -r /tmp/openmediavault-monitoring-odroid-xu4-master

chmod +x /usr/local/bin/cputemp /usr/share/openmediavault/mkconf/collectd.d/cpu{freq,temp}
omv-mkconf collectd

chown openmediavault:openmediavault /var/www/openmediavault/js/omv/module/admin/diagnostic/system/plugin/Cpu{Temperature,Frequency}.js
chmod 644 /var/www/openmediavault/js/omv/module/admin/diagnostic/system/plugin/Cpu{Temperature,Frequency}.js

source /usr/share/openmediavault/scripts/helper-functions && omv_purge_internal_cache
```

## Examples
![CPU Frequency](http://obihoernchen.net/wordpress/wp-content/uploads/2015/10/Screenshot-from-2015-10-20-18-56-20.png)
![CPU Temperature](http://obihoernchen.net/wordpress/wp-content/uploads/2015/10/Screenshot-from-2015-10-20-18-56-42.png)
