#!/bin/bash 

MACHINE_NAME="$(uname -s)"

# Thanks to https://stackoverflow.com/questions/3466166/how-to-check-if-running-in-cygwin-mac-or-linux
case "${MACHINE_NAME}" in
    Linux*)     OS=Linux;;
    Darwin*)    OS=Mac;;
	CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${MACHINE_NAME}"
esac

> ./my_app/tables/__init__.py
for file in ./my_app/tables/*; do
  FNAME=${file##*/}

  if [ $FNAME = "__init__.py" ] || [ $FNAME = "__pycache__" ] || [ $FNAME = "base.py" ];then
  	echo "CHEESE"
  else 
  	i=$((${#FNAME}-3))
  	TABLENAME="${FNAME:0:$i}"
  	# If problem with sed -r on Mac run ```brew install gnu-sed```
  	if [[ $OS = "Mac" ]]; then
  		CAMELCASED=`echo $TABLENAME | gsed -r 's/(^|_)([a-z])/\U\2/g'`
  	else
  		CAMELCASED=`echo $TABLENAME | sed -r 's/(^|_)([a-z])/\U\2/g'`
  	fi
  	echo "from .$FNAME import $CAMELCASED" >> ./my_app/tables/__init__.py
  fi
done

# for file in ./my_app/models/*; do
#   FNAME=${file##*/}
#   if [ $FNAME = "__init__.py" ] || [ $FNAME = "__pycache__" ] || [ $FNAME = "base.py" ];then
#   	echo "pass"
#   else 
#   	echo $FNAME
#   fi
# done

# for file in ./my_app/models/*; do
#   # echo ${file##*/}
#   if
#   ARRAY+=(${file##*/})
# done

# for file in ./my_app/models/*; do
#   # echo ${file##*/}
#   ARRAY+=(${file##*/})
# done