const calculadora = {
    sumar() {
       // debugger; // Punt d'aturada 1
        
        const a = 15;
        const b = 3;
        const resultat = a + b;
        
        this.mostrarResultat(`Suma: ${a} + ${b} = ${resultat}`);
    },
    
    multiplicar() {
        //debugger; // Punt d'aturada 2
        
        const a = 6;
        const b = 7;
        const resultat = a * b;
        
        this.mostrarResultat(`Multiplicació: ${a} × ${b} = ${resultat}`);
    },
    
    mostrarResultat(missatge) {
        const element = document.getElementById('resultat');
        element.textContent = missatge;
        console.log(missatge);
    }
};