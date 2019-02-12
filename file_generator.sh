#!/bin/bash 

CURR_DIR=`pwd`
echo $CURR_DIR

# for file in "$CURR_DIR/my_app/*"
# do
# 	echo $file
# done;

ARRAY=()

for file in ./my_app/models/*; do
  # echo ${file##*/}
  ARRAY+=(${file##*/})
done

for file in ./my_app/models/*; do
  # echo ${file##*/}
  if
  ARRAY+=(${file##*/})
done

for file in ./my_app/models/*; do
  # echo ${file##*/}
  ARRAY+=(${file##*/})
done

echo "${ARRAY[*]}"

