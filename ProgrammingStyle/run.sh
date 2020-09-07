#!/bin/bash

function msg() {
    echo "$@"
}

function date_diff() {
	date -u -d @"$(($2 - $1))" +"%-Hh %-Mm %-Ss"
}

cd $(dirname $0)

mydir=$(pwd)
if [ -z "$1" ]; then
  items=$(echo ./[0-9][0-9]-*/)
else
  items=./$1-*
fi

total=0
fail=0
result_file=$mydir/res/result.txt
input_file=$mydir/res/pride-and-prejudice.txt

suite_start=$(date +"%s")
for dir in $items; do
  script_file=$(echo $(basename $dir/*.py))
  if [ -x $dir/$script_file ]; then
    msg $(date +%T) testing $(basename $dir)/$script_file with $(basename $input_file)

    expected=$result_file
    test_start=$(date +"%s")
    actual=$($dir/$script_file $input_file | grep -)
    test_end=$(date +"%s")

    echo "$actual" | diff -b $expected - > /dev/null
    result=$?
    total=$((total + 1))
    if [ $result -ne 0 ]; then
      echo
      echo " Expected     Actual"
      echo "----------   --------"
      echo "$actual" | paste $expected - | column -t
      echo
      fail=$(($fail + 1))
      msg $exe FAILED in $(date_diff $test_start $test_end)!
    else
      msg $exe PASSED in $(date_diff $test_start $test_end).
    fi
  fi
done
suite_end=$(date +"%s")

msg Ran $total tests with $fail failures in $(date_diff $suite_start $suite_end).
if [ $fail -ne 0 ]; then
    msg FAILED!
    exit $fail
fi
msg PASSED