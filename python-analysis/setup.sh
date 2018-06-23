# Source this script to set up analysis in this directory tree

if [ "x${BASH_ARGV[0]}" = "x" ]; then
    THIS="."
else
    THIS=$(dirname ${BASH_ARGV[0]})
    if [ "${THIS:0:1}" != "/" ]; then
	[ "${THIS}" = "." ] && unset THIS
	THIS=${THIS%/}
	THIS=$PWD/$THIS
	THIS=${THIS%/}
    fi
fi

[ -z "$WORKSHOP_DATA" ] && export WORKSHOP_DATA=/data

if [ ! -e ${THIS}/data ]; then
    if [ ! -z "$WORKSHOP_DATA" -a -r ${WORKSHOP_DATA}/ROOTfiles/python-analysis ]; then
	ln -s ${WORKSHOP_DATA}/ROOTfiles/python-analysis ${THIS}/data
    elif [ -r ${THIS}/../rootfiles/python-analysis ]; then
	ln -s ${THIS}/../rootfiles/python-analysis ${THIS}/data
    else
	echo "$WORKSHOP_DATA/ROOTfiles/python-analysis not found. Creating empty data dir"
	echo "You must add root files for the Python examples to work"
	mkdir ${THIS}/data
    fi
fi
