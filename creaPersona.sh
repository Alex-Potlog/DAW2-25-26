# Usa este script para añadir a alguien al proyecto, para usarlo
# pon ./creaPesona.sh nombre-persona
# y luego haz git add . && git commit -m Añadir persona encapsulado en  "
mkdir $1
cd $1
mkdir M6
mkdir M7
mkdir M8
mkdir M9
mkdir MOPT
find . -mindepth 1 -maxdepth 2 -type d -exec touch {}/archivo.txt \;
