
# openmediavault-monitoring-odroid-xu4
Some additional RRDTool graphs for OpenMediaVault Monitoring for your ODROID-XU4.
Should work for ODROID-XU3 as well.



## Installation
```Shell
cd /tmp
wget https://github.com/obihoernchen/openmediavault-monitoring-odroid-xu4/archive/master.zip
unzip master.zip
cd openmediavault-monitoring-odroid-xu4-master
cp -R usr/* /usr
cp -R var/* /var
rm -r /tmp/openmediavault-monitoring-odroid-xu4-master
cd /

chmod +x /usr/local/bin/cpu{temp,fanspeed} /usr/share/openmediavault/mkconf/collectd.d/cpu{freq,temp,fanspeed} 
chmod +x /usr/share/openmediavault/mkrrdgraph/plugins.d/*.py

omv-mkconf collectd

chown openmediavault-webgui:openmediavault-webgui /var/www/openmediavault/js/omv/module/admin/diagnostic/system/plugin/Cpu{Temperature,Frequency,FanSpeed}.js
chmod 644 /var/www/openmediavault/js/omv/module/admin/diagnostic/system/plugin/Cpu{Temperature,Frequency,FanSpeed}.js

source /usr/share/openmediavault/scripts/helper-functions && omv_purge_internal_cache

# optionally add the below two lines without # symbols to /etc/default/openmediavault
# OMV_COLLECTD_RRDTOOL_GRAPH_WIDTH=800
# OMV_COLLECTD_RRDTOOL_GRAPH_HEIGHT=200

omv-mkconf collectd
omv-mkconf rrdcached

reboot
```

## Examples
![CPU Frequency](http://obihoernchen.net/wordpress/wp-content/uploads/2015/10/Screenshot-from-2015-10-20-18-56-20.png)
![CPU Temperature](http://obihoernchen.net/wordpress/wp-content/uploads/2015/10/Screenshot-from-2015-10-20-18-56-42.png)
