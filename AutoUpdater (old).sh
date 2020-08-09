#!/usr/bin/env bash

update () {
	# arg1: command, arg2: string for no change, arg3: title of notification
	echo -e "\t$1" >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/output_log.txt
	output=$($1)
	echo -e "\t\t$output\n" >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/output_log.txt
	if [ $# -eq 3 ]; then
		[ output != "$2" ]
	else
		[ "$(echo ${output:$4:$5})" == "$2" ]
	fi
	if [ $? = 1 ]; then
		printf -v notif "display notification \"%s\" with title \"%s\" subtitle \"AutoUpdater\" sound name \"Ping\"" "$output" "$3"
		osascript -e "$notif"
		if [ $added -eq 0 ]; then
			echo $(date) >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/changes.txt
			added=1
		fi
		echo -e "\t$1" >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/changes.txt
		echo -e "\t\t$output\n" >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/changes.txt
	fi
}

echo $(date) >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/output_log.txt
added=0

# # brew cask upgrade
update "brew cask upgrade" "==> No Casks to upgrade" "Casks Updated!"

# # brew upgrade
update "brew upgrade" "" "Brew Updated!"

# pip install -U pip
update "pip install -U pip" "Requirement already up-to-date:" "Pip Updated!" 0 31

# # rvm install ruby@latest
update "rvm install ruby@latest" "Ruby Updated!" 

# divider for output_log.txt
echo -e "———————————————————————————————————————————————————————————————————————————————————————————————————"'\n' >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/output_log.txt

# conditional divder for changes.txt
if [ $added -eq 1 ]; then
	echo -e "———————————————————————————————————————————————————————————————————————————————————————————————————"'\n' >> /Users/Michael/Documents/Programming/python/projects/AutoUpdater/changes.txt
fi