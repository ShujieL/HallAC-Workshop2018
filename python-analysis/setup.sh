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

echo "python-analysis THIS: ${THIS}"

[ -e ${THIS}/data ] || ln -s /data/ROOTfiles/python-analysis ${THIS}/data
