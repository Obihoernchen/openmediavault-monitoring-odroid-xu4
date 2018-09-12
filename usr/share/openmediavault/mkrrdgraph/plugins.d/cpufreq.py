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
                        'title_cpu': 'CPU frequency',
                        'color_canvas': '#ffffff',
                        'color_cpu_a15': '#ff0000',
                        'color_cpu_a07': '#0000fd'
                })
                args = []
                args.append('{image_dir}/cpufreq-{period}.png'.format(**config))
                args.extend(config['defaults'])
                args.extend(['--start', config['start']])
                args.extend(['--title', '"{title_cpu}{title_by_period}"'.format(**config)])
                args.append('--slope-mode')
                args.extend(['--lower-limit', '0'])
                args.extend(['--vertical-label', 'Hz'])
                args.append('DEF:cpu_a15_avg={data_dir}/cpufreq/cpufreq-4.rrd:value:AVERAGE'.format(**config))
                args.append('DEF:cpu_a07_avg={data_dir}/cpufreq/cpufreq-0.rrd:value:AVERAGE'.format(**config))
                args.append('DEF:cpu_a15_min={data_dir}/cpufreq/cpufreq-4.rrd:value:MIN'.format(**config))
                args.append('DEF:cpu_a07_min={data_dir}/cpufreq/cpufreq-0.rrd:value:MIN'.format(**config))
                args.append('DEF:cpu_a15_max={data_dir}/cpufreq/cpufreq-4.rrd:value:MAX'.format(**config))
                args.append('DEF:cpu_a07_max={data_dir}/cpufreq/cpufreq-0.rrd:value:MAX'.format(**config))
                args.append('LINE1:cpu_a15_avg{color_cpu_a15}:"Cortex-A15"'.format(**config))
                args.append('GPRINT:cpu_a15_min:MIN:"%5.1lf%s Min"'.format(**config))
                args.append('GPRINT:cpu_a15_avg:AVERAGE:"%5.1lf%s Avg"'.format(**config))
                args.append('GPRINT:cpu_a15_max:MAX:"%5.1lf%s Max"'.format(**config))
                args.append('GPRINT:cpu_a15_avg:LAST:"%5.1lf%s Last\l"'.format(**config))
                args.append('LINE1:cpu_a07_avg{color_cpu_a07}:"Cortex-A7 "'.format(**config))
                args.append('GPRINT:cpu_a07_min:MIN:"%5.1lf%s Min"'.format(**config))
                args.append('GPRINT:cpu_a07_avg:AVERAGE:"%5.1lf%s Avg"'.format(**config))
                args.append('GPRINT:cpu_a07_max:MAX:"%5.1lf%s Max"'.format(**config))
                args.append('GPRINT:cpu_a07_avg:LAST:"%5.1lf%s Last\l"'.format(**config))
                args.append('COMMENT:"{last_update}"'.format(**config))
                openmediavault.mkrrdgraph.call_rrdtool_graph(args)
                return 0

