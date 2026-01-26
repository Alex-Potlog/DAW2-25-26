from django.shortcuts import render

# Create your views here.


def personatge(request):
    context = {
        'nom': 'Gandalf',
        'classe': 'Mag',
        'raça': 'Maiar',
        'nivell': 10,
        'stats': {
            'for': 10,
            'des': 14,
            'con': 12,
            'int': 18,
            'sab': 16,
            'car': 15,
        },
        'habilitats': ['Llançar encanteris',
                       'Coneixement de màgia antiga',
                       'Manipulació d\'energies',],
        'equipament': [
            'Bastó màgic',
            'Robes de mag',
            'Llibre d\'encanteris',
        ],
    }
    return render(request, 'personatge.html', context)
