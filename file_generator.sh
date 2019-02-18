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

function write_file(){
  echo $1
  for file in $1*; do
  FNAME=${file##*/}
  echo "name is $FNAME"

  if [ $FNAME = "__init__.py" ] || [ $FNAME = "__pycache__" ] || [ $FNAME = "base.py" ];then
    echo "CHEESE"
  else 
    i=$((${#FNAME}-3))
    TABLENAME="${FNAME:0:$i}"
    # If problem with sed -r on Mac run ```brew install gnu-sed```
    # This converts to file name to a CamelCase (whcih should be the class name)
    if [[ $OS = "Mac" ]]; then
      CAMELCASED=`echo $TABLENAME | gsed -r 's/(^|_)([a-z])/\U\2/g'`
    else
      CAMELCASED=`echo $TABLENAME | sed -r 's/(^|_)([a-z])/\U\2/g'`
    fi
    echo "writing"
    echo "from .$TABLENAME import $CAMELCASED" >> $1/__init__.py
  fi
done
}

> ./my_app/tables/__init__.py

write_file ./my_app/tables/

# Writing the head of the models __init__ to create a Sql Base
for i in "$(cat ./utilities/models_head.txt)"; 
do echo "$i">./my_app/models/__init__.py; done

write_file ./my_app/models/
# echo "$(cat ./utilities/models_head.txt)"
# for file in ./my_app/models/*; do
#   FNAME=${file##*/}
#   if [ $FNAME = "__init__.py" ] || [ $FNAME = "__pycache__" ] || [ $FNAME = "base.py" ];then
#   	echo "CHEESE"
#   else 
#   	i=$((${#FNAME}-3))
#   	TABLENAME="${FNAME:0:$i}"
#   	# If problem with sed -r on Mac run ```brew install gnu-sed```
#   	# This converts to file name to a CamelCase (whcih should be the class name)
#   	if [[ $OS = "Mac" ]]; then
#   		CAMELCASED=`echo $TABLENAME | gsed -r 's/(^|_)([a-z])/\U\2/g'`
#   	else
#   		CAMELCASED=`echo $TABLENAME | sed -r 's/(^|_)([a-z])/\U\2/g'`
#   	fi
#   	echo "from .$TABLENAME import $CAMELCASED" >> ./my_app/models/__init__.py
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