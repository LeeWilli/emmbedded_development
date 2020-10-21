#!/bin/bash

function trigger_bright {
# $1 is for cycle, $2 is for duty cycle
	cd /sys/class/leds/led0
	sudo sh -c "echo timer > trigger"
	sleep 1
	ls
	sudo sh -c "echo $2 > delay_on"
	sudo sh -c "echo $[$1-$2] > delay_off"
	echo delay_on is 
	cat delay_on
	echo delay_off is
	cat delay_off
	sleep 10
	sudo sh -c "echo mmc0 > trigger"
	sleep 1
}


trigger_bright 10 1 
trigger_bright 10 5 
trigger_bright 10 9 
