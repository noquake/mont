#! /bin/sh

# check for current usb devices connected to machine
check_devices()
{
echo During installation mont will get a snapshot of the devices connected to this machine. Are there any current usb connections? y/n \n
read INPUT=${INPUT:-y}

if [$INPUT="y"]
	then echo Please remove connected devices and retry the installation afterwards. Thank you !
		exit
	elif [$INPUT="n"];
		break
	else
		check_devices()
fi
}

# initialize /dev state
get_state() {
	local directory=$directory
	local output=$output

	ls "$directory" >> ~/mont/.state/$output.txt
}

# combine original + new state and find uniq devices
get_newdev() {
	ostate="~/mont/.state/ostate.txt"
	nstate="~/mont/.state/nstate.txt"

	cat ostate nstate > temp && uniq temp > temp
}

