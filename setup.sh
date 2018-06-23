# Source this script to set up analysis in this directory tree
# Assumes ROOT and ANALYZER are set up (done in ~/.bash_profile login script)

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

if [ ! -e ${THIS}/data ]; then
    if [ ! -z "$WORKSHOP_DATA" -a -r ${WORKSHOP_DATA}/raw ]; then
	ln -s ${WORKSHOP_DATA}/raw ${THIS}/data
    elif [ -r /data/raw ]; then
	ln -s /data/raw ${THIS}/data
    else
	echo "/data/raw not found, creating empty data dir"
	mkdir ${THIS}/data
    fi
fi
if [ ! -e ${THIS}/rootfiles ]; then
    if [ ! -z "$WORKSHOP_DATA" -a -r ${WORKSHOP_DATA}/ROOTfiles ]; then
	ln -s ${WORKSHOP_DATA}/ROOTfiles ${THIS}/rootfiles
    elif [ -r /data/ROOTfiles ]; then
	ln -s /data/ROOTfiles ${THIS}/rootfiles
    else
	echo "/data/ROOTfiles not found, creating empty rootfiles dir"
	mkdir ${THIS}/rootfiles
    fi
fi

[ -e ${THIS}/python-analysis ] && . ${THIS}/python-analysis/setup.sh

export DB_DIR=${THIS}/DB
export DATA_DIR=${THIS}/data
export OUT_DIR=${THIS}/rootfiles

