#!/bin/bash
# Created by XH
date
echo none > /sys/class/leds/led0/trigger
echo "Duty ratio = 1.0 1000Hz"
echo 1 > /sys/class/leds/led0/brightness
sleep 10

echo "Duty ratio = 0.5 500Hz"
for((i=0; i<1000; i++))
do
	echo 0 > /sys/class/leds/led0/brightness
	sleep 0.001
	echo 1 > /sys/class/leds/led0/brightness
	sleep 0.001
done

echo "Duty ratio = 0.1 100Hz"
for((i=0; i<1000; i++))
do
	echo 0 > /sys/class/leds/led0/brightness
	sleep 0.009
	echo 1 > /sys/class/leds/led0/brightness
	sleep 0.001
done

echo mmc0 > /sys/class/leds/led0/trigger
date
