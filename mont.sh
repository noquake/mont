#! /bin/sh
. ./functions.sh

echo searching for new drives... \n

# get the new state of the /dev directory 
get_state("/dev" "cstate")

cd ~

if /[MOUNTED DRIVES] !exist mkdir /[MOUNTED DRIVES]

cd /
# check if a new drive has been connected via some kind of system prompt
for [FOUND DRIVES]
	add to list
fi

for [DRIVE] in [FOUND DRIVE LIST] 
	mount [DRIVE] ~/[MOUNTED DRIVES]/

fi

