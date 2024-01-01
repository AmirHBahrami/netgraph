#!/usr/bin/bash

# XXX NOTE: run this script from the parent directory not 
# it's own directory

declare -a website_lists=(
	"unix.stackexchange.com" 	"www.freecodecamp.org"
	"stackoverflow.com" 	"www.baeldung.com"
	"superfastpython.com"	"docs.python.org"
	"businessnamegenerator.com" "www.namebounce.com"
	"namelix.com" "www.nameboy.com "
)

#for w in "${website_lists[@]}"
#do
python3 . "${website_lists[@]}" -o "./data/${date}.json" -v
#done
