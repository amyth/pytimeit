#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
#    PyTimeit v. 0.1
#
#    Copyright (C) 2014  Amyth Arora
#    @Author - Amyth Arora <mail@amythsingh.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; Applies version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import time
import uuid


class TimeLogger(object):
    """ Logs the time taken to run a certain piece of code.
    """

    def __init__(self, debug=True):
        """ Called when the TimeLogger class is initialized
        """

        self.processes = {}
        self.decimals = 3
        self.prediction_offset = 2
        self.debug = debug

        # Text format for printing messages
        self.text_format = {
            'bold': '\033[01m',
            'error': '\033[91m',
            'info': '\033[94m',
            'success': '\033[92m',
            'warning': '\033[93m',
            'end_col': '\033[0m',
        }

    def _float(self, item):
        """
        Converts the given item to a float and limits
        the decimal places to what's defined on initialization.
        """

        frmt = "{0:.%sf}" % (self.decimals)
        return float(frmt.format(item))

    def to_seconds(self, item):
        """
        Converts a given item to a seconds format output
        """

        return "%s second(s)" % self._float(item)

    def print_time(self, process):
        """ Prints the message according to the given msg_type
        """

        bold = self.text_format['bold']
        end_col = self.text_format['end_col']

        # Configure message type
        predicted = process['predicted']
        time_taken = process['actual_time_taken']
        if time_taken < predicted:
            msg_type = self.text_format['success']
        elif (time_taken > predicted) and (time_taken < (
            predicted * self.prediction_offset)):
            msg_type = self.text_format['warning']
        elif (time_taken > predicted * self.prediction_offset):
            msg_type = self.text_format['error']
        else:
            msg_type = self.text_format['info']

        message = "\n%s%s%s%s: Total time taken was %s%s%s" % (bold,
                msg_type, process['message'], end_col,
                msg_type, process['time_taken'], end_col)

        print message

    def record_time_process(self, message, predicted=1):
        """
        Creates a new time alculation process and adds it
        to self.processes
        """

        start = time.time()
        process_id = uuid.uuid4().hex
        process = {
            'start': start,
            'message': message,
            'predicted': predicted,
        }
        self.processes[process_id] = process

        return process_id


    def stop_recording(self, process_id):
        """
        Stops recording the time for a process.
        """

        stop = time.time()
        process = self.processes.get(process_id)
        process['stop'] = stop
        time_taken = stop - process['start']
        process['actual_time_taken'] = time_taken
        process['time_taken'] = self.to_seconds(time_taken)

        if self.debug:
            self.print_time(process)
