#!/bin/bash
echo "---===<<[[System Status]]>>===---"
echo "__//{System Name: '$(hostname)'}\\\\__"
echo "          <<<CPU>>>"
cat /proc/cpuinfo | grep -m 1 'model name'
echo "cpu cores       : $(cat /proc/cpuinfo | grep processor | wc -l)"
cat /proc/cpuinfo | grep -m 1 'cpu MHz'
cat /proc/cpuinfo | grep -m 1 'cache size'
echo "          <<<RAM>>>"
cat /proc/meminfo | grep MemTotal
cat /proc/meminfo | grep MemFree
echo "          <<<HDD>>>"
df -h 2>&1 | grep -v 'tmpfs' 
echo "          <<<NET>>>"
echo "Iface:     IP address:"
for DEV in /sys/class/net/*; do printf "%-10s %s\n" ${DEV##*/} $(ifconfig ${DEV##*/} | \sed -rne '/inet addr/s/\s+inet addr:([0-9.]+).*/\1/gp'); done
echo " "
echo "Testing internet connectivity . . ."
wget -q --spider http://google.com

if [ $? -eq 0 ]; then
    echo "                                    \\\\>>:Online"
else
    echo "                                    \\\\>>:Offline"
fi
echo "          <<<O_S>>>"
echo "Kernel:         $(uname -r)"
lsb_release -a 2>&1 | grep -v "No LSB modules are available."
echo "        <<<SESSION>>>"
echo "User:       $(whoami)"
echo "ID:         $(id -u)"
echo "Login:$(last | grep 'still logged in\|gone - no logout' | sed 's/^[^\:]\+\://' | cut -c 11-32)" 
echo "Time:      $(uptime | grep 'up' | cut -d , -f 1)" 
