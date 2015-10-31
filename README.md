# openmediavault-monitoring-odroid-xu4
Some additional RRDTool graphs for OpenMediaVault Monitoring for your ODROID-XU4.
Should work for ODROID-XU3 as well.

## Installation
Copy all files to their path. Then execute the following commands as root:
```Shell
chmod +x /usr/local/bin/cputemp /usr/share/openmediavault/mkconf/collectd.d/cpu{freq,temp}
omv-mkconf collectd

chown openmediavault:openmediavault /var/www/openmediavault/js/omv/module/admin/diagnostic/system/plugin/Cpu{Temperature,Frequency}.js
chmod 644 /var/www/openmediavault/js/omv/module/admin/diagnostic/system/plugin/Cpu{Temperature,Frequency}.js

source /usr/share/openmediavault/scripts/helper-functions && omv_purge_internal_cache
```