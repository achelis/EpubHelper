#!/bin/bash
pushd $1
for f in chapter* 
do
  c=`echo $f | sed -e "s_[a-z]*\([0-9]*\)\.html_\1_"`
  t=${f}.tmp
  # Clean up starts here
  sed -i -e "s_\ 1\ _ I _g" $f
  grep -v "WE[I1][S5]\s*AND\s*H[I1]CKMAN" $f > $t
  grep -v ">.\{0,2\}v\s\{0,1\}e\s\{0,1\}n\s\{0,10\}S\s\{0,1\}t\s\{0,1\}a\s\{0,1\}r.\{0,3\}<" $t > $f
  grep -v ">.\{0,3\}[0-9]\{1,3\}.\{0,3\}<" $f > $t
  mv $t $f
  sed -i -e "s_.*>\s*CHAPTER.*_<h1 class=\"chapter\">Chapter ${c}</h1>_" $f
  # ends here
done
popd
