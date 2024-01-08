#!/bin/bash

TC=/sbin/tc

# Interface traffic will leave on
IF=eth0

# Latency in milliseconds
LATENCY=50ms

# Broker
DST_CIDR=172.100.10.10/32

# Filter command -- add ip dst match at the end
U32="$TC filter add dev $IF protocol ip parent 1:0 prio 1 u32"

create () {
  echo "== SHAPING INIT =="

  # Create the root qdisc
  $TC qdisc add dev $IF root handle 1:0 htb \
    default 30

  # Introduce latency using netem qdisc
  $TC qdisc add dev $IF parent 1:0 handle 2: netem delay $LATENCY

  # Setup filters to ensure packets are enqueued to the correct
  # child based on the src IP of the packet
  $U32 match ip dst $DST_CIDR flowid 1:0

  echo "== SHAPING DONE =="
}

# Run clean to ensure existing tc is not configured
clean () {
  echo "== CLEAN INIT =="
  $TC qdisc del dev $IF root
  echo "== CLEAN DONE =="
}

clean
create