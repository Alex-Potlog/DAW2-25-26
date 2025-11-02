function guardar_info(){
    const nom = document.getElementById("nom").value;
    const cognom = document.getElementById("cognom").value;
    const email = document.getElementById("email").value;
    const adreca = document.getElementById("adreca").value;

    localStorage.setItem("nom", nom);
    localStorage.setItem("cognom", cognom);
    localStorage.setItem("email", email);
    localStorage.setItem("adreca", adreca);
    
    console.log("Dades guardades en Local Storage");
}

const boto = document.getElementById("enviar");
boto.addEventListener("click", guardar_info);

function escriure(){
    const nom = document.getElementById("nom");
    const cognom = document.getElementById("cognom");
    const email = document.getElementById("email");
    const adreca = document.getElementById("adreca");

    nom.value = localStorage.getItem("nom") || "";
    cognom.value = localStorage.getItem("cognom") || "";
    email.value = localStorage.getItem("email") || "";
    adreca.value = localStorage.getItem("adreca") || "";
}

document.addEventListener("DOMContentLoaded", escriure);

function eliminarDades(){
    localStorage.removeItem("nom");
    localStorage.removeItem("cognom");
    localStorage.removeItem("email");
    localStorage.removeItem("adreca");
    
    // Netejar el formulari
    document.getElementById("nom").value = "";
    document.getElementById("cognom").value = "";
    document.getElementById("email").value = "";
    document.getElementById("adreca").value = "";
    
}

const botoReset = document.getElementById("eliminar");
botoReset.addEventListener("click", eliminarDades);