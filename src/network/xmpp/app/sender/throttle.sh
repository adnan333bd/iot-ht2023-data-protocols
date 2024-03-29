#!/bin/bash

TC=/sbin/tc

# interface traffic will leave on
IF=eth0

# The parent limit, children can borrow from this amount of bandwidth
# based on what's available.
LIMIT=3kbit

# broker
DST_CIDR=172.100.39.10/32

# filter command -- add ip dst match at the end
U32="$TC filter add dev $IF protocol ip parent 1:0 prio 1 u32"

create () {
  echo "== SHAPING INIT =="

  # create the root qdisc
  $TC qdisc add dev $IF root handle 1:0 htb \
    default 30

  # create the parent qdisc, children will borrow bandwidth from
  $TC class add dev $IF parent 1:0 classid \
    1:1 htb rate $LIMIT

  # setup filters to ensure packets are enqueued to the correct
  # child based on the src IP of the packet
  $U32 match ip dst $DST_CIDR flowid 1:1

  echo "== SHAPING DONE =="
}

# run clean to ensure existing tc is not configured
clean () {
  echo "== CLEAN INIT =="
  $TC qdisc del dev $IF root
  echo "== CLEAN DONE =="
}

clean
create