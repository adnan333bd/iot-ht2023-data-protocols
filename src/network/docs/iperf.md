iperf3 -s -p 8080

source / broker
iperf3 -c 172.100.10.15 -p 8080 -t 30

dest / subscriber
iperf3 -s -p 8080