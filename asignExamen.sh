nom=$1
mkdir "Examen-${nom}"
cd "Examen-${nom}"
mkdir apuntes
mkdir ejercicios
find . -mindepth 1 -maxdepth 2 -type d -exec touch {}/archivo.txt \;
