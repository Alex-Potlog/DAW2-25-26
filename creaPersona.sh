mkdir $1
cd $1
mkdir M6
mkdir PHP
mkdir M8
mkdir M9
mkdir Python
find . -mindepth 1 -maxdepth 2 -type d -exec touch {}/archivo.txt \;
