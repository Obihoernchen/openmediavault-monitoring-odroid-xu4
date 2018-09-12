# -*- coding: utf-8 -*-
#
# This file is part of OpenMediaVault.
#
# @license   http://www.gnu.org/licenses/gpl.html GPL Version 3
# @author    Volker Theile <volker.theile@openmediavault.org>
# @copyright Copyright (c) 2009-2018 Volker Theile
#
# OpenMediaVault is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# OpenMediaVault is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenMediaVault. If not, see <http://www.gnu.org/licenses/>.
import openmediavault.mkrrdgraph
import openmediavault.subprocess

class Plugin(openmediavault.mkrrdgraph.IPlugin):
        def create_graph(self, config):
                # http://paletton.com/#uid=33r0-0kwi++bu++hX++++rd++kX
                config.update({
                        'title_cpufanspeed': 'CPU fan speed',
                        'color_canvas': '#ffffff',
                        'color_cpufanspeed': '#ff0000',
                        'color_cpufanspeedtrans': '#ff000044'
                })
                args = []
                args.append('{image_dir}/cpufanspeed-{period}.png'.format(**config))
                args.extend(config['defaults'])
                args.extend(['--start', config['start']])
                args.extend(['--title', '"{title_cpufanspeed}{title_by_period}"'.format(**config)])
                args.append('--slope-mode')
                args.extend(['--upper-limit', '100'])
                args.extend(['--lower-limit', '0'])
                args.extend(['--rigid'])
                args.extend(['--vertical-label', 'Percent'])
                args.append('DEF:cpufanspeed_avg={data_dir}/fanspeed/fanspeed.rrd:value:AVERAGE'.format(**config))
                args.append('DEF:cpufanspeed_min={data_dir}/fanspeed/fanspeed.rrd:value:MIN'.format(**config))
                args.append('DEF:cpufanspeed_max={data_dir}/fanspeed/fanspeed.rrd:value:MAX'.format(**config))
                args.append('AREA:cpufanspeed_max{color_cpufanspeedtrans}'.format(**config))
                args.append('AREA:cpufanspeed_min{color_canvas}'.format(**config))
                args.append('LINE1:cpufanspeed_avg{color_cpufanspeed}:"Speed"'.format(**config))
                args.append('GPRINT:cpufanspeed_min:MIN:"%5.1lf%s Min"'.format(**config))
                args.append('GPRINT:cpufanspeed_avg:AVERAGE:"%5.1lf%s Avg"'.format(**config))
                args.append('GPRINT:cpufanspeed_max:MAX:"%5.1lf%s Max"'.format(**config))
                args.append('GPRINT:cpufanspeed_avg:LAST:"%5.1lf%s Last\l"'.format(**config))
                args.append('COMMENT:"{last_update}"'.format(**config))
                openmediavault.mkrrdgraph.call_rrdtool_graph(args)
                return 0