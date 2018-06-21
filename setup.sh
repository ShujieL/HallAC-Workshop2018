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

[ -e ${THIS}/data ] || ln -s /data/raw ${THIS}/data
[ -e ${THIS}/rootfiles ] || ln -s /data/ROOTfiles ${THIS}/rootfiles

[ -e ${THIS}/python-analysis ] && . ${THIS}/python-analysis/setup.sh

export DB_DIR=${THIS}/DB
export DATA_DIR=${THIS}/data
export OUT_DIR=${THIS}/rootfiles

