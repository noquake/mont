#! /bin/sh

# import functions
. ./functions.sh

# welcome
echo Welcome to mont! \n

# check for current usb devices connected to machine
check_devices()

# make mont directory/subfolder 
mkdir ~/.mont

# get initial state of [/dev] directory
get_state "/dev" "ostate"

echo mont has been initialized! 
echo To use plug in your desired usb device and run 'mont' to mount the device and have it available directly in your home directory.
