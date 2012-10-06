#!/bin/bash
# TODO - make these configurable
# For now change these variables to change tmp folder and output epub filename
TMP_DIR=tmp
OUTPUT=clean.epub
[[ -d $TMP_DIR ]] && rm -rf $TMP_DIR
unzip "$1" -d ${TMP_DIR}

for f in ${TMP_DIR}/index* 
do
  echo "Normalizing: ${f}"
  ./normalize.py $f  > ${f}.new
  mv ${f}.new $f
done
./chapters.py ${TMP_DIR}

rm ${TMP_DIR}/index*

./clean.sh ${TMP_DIR}

pushd ${TMP_DIR}
  [[ -e ../${OUTPUT} ]] && rm ../${OUTPUT}
  zip -r ../${OUTPUT} *
popd
