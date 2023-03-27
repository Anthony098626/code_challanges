#!/user/bin/env python3

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/27/2023
# Creates: python script performing verious functions

import psutil
import time
import os

# Get CPU time information
cpu_times = psutil.cpu_times()

# Get CPU time spent by normal processes
user_time = cpu_times.user

# Get CPU time spent by processes executing in kernel mode
system_time = cpu_times.system

# Get time when system was idle
idle_time = cpu_times.idle

# Get CPU time spent by priority processes executing in user mode
priority_user_time = cpu_times.nice

# Get time spent waiting for I/O to complete
io_time = cpu_times.iowait

# Get time spent for servicing hardware interrupts
irq_time = cpu_times.irq

# Get time spent for servicing software interrupts
softirq_time = cpu_times.softirq

# Get time spent by other operating systems running in a virtualized environment
steal_time = cpu_times.steal

# Get time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
guest_time = cpu_times.guest

# Save the CPU time information to a text file
with open('cpu_time.txt', 'w') as f:
    f.write(f'Time spent by normal processes executing in user mode: {user_time}\n')
    f.write(f'Time spent by processes executing in kernel mode: {system_time}\n')
    f.write(f'Time when system was idle: {idle_time}\n')
    f.write(f'Time spent by priority processes executing in user mode: {priority_user_time}\n')
    f.write(f'Time spent waiting for I/O to complete: {io_time}\n')
    f.write(f'Time spent for servicing hardware interrupts: {irq_time}\n')
    f.write(f'Time spent for servicing software interrupts: {softirq_time}\n')
    f.write(f'Time spent by other operating systems running in a virtualized environment: {steal_time}\n')
    f.write(f'Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {guest_time}\n')

# Email the text file to yourself using Sendmail
os.system('echo "Here is the CPU time information." | mailx -s "CPU time information" -a "cpu_time.txt" anthony098626@gmail.com')

# sources: https://chat.openai.com/chat