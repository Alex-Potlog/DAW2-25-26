#!/bin/bash
#Para utilizar el scss hay que hacer un conjunto de carpetas y archivos en el proyecto
#Utiliza los siguientes comandos para crearlo todo

mkdir public

cd public

mkdir css fonts html img js

echo "<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>" > html/index.html

cd ..

mkdir styles
cd styles
mkdir abstracts base components layout pages themes vendors
touch style.scss
echo "@use 'abstracts' as *;" >> style.scss
echo "@use 'base' as *;" >> style.scss
echo "@use 'components' as *;" >> style.scss
echo "@use 'layout' as *;" >> style.scss
echo "@use 'pages' as *;" >> style.scss
echo "@use 'themes' as *;" >> style.scss
echo "@use 'vendors' as *;" >> style.scss

cd abstracts
touch _variables.scss _mixins.scss _functions.scss _placeholders.scss
echo "@forward 'variables';" > _index.scss
echo "@forward 'mixins';" >> _index.scss
echo "@forward 'functions';" >> _index.scss
echo "@forward 'placeholders';" >> _index.scss

cd ../base
touch _reset.scss _typography.scss _base.scss
echo "@forward 'base';" > _index.scss
echo "@forward 'reset';" >> _index.scss
echo "@forward 'typography';" >> _index.scss

cd ../components
touch _buttons.scss _forms.scss _navigation.scss _cards.scss
echo "@forward 'buttons';" > _index.scss
echo "@forward 'cards';" >> _index.scss
echo "@forward 'forms';" >> _index.scss
echo "@forward 'navigation';" >> _index.scss

cd ../layout
touch _header.scss _footer.scss _grid.scss _sidebar.scss
echo "@forward 'footer';" > _index.scss
echo "@forward 'grid';" >> _index.scss
echo "@forward 'header';" >> _index.scss
echo "@forward 'sidebar';" >> _index.scss

cd ../pages
touch _home.scss _about.scss
echo "@forward 'about';" > _index.scss
echo "@forward 'home';" >> _index.scss

cd ../themes
touch _light.scss _dark.scss
echo "@forward 'dark';" > _index.scss
echo "@forward 'light';" >> _index.scss

cd ../vendors
touch _bootstrap.scss
echo "@forward 'bootstrap';" > _index.scss
