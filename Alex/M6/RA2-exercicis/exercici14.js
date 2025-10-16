function afegirElement() {
    let input = document.createElement("input");
    input.type = "email";
    input.name = "email";
    input.placeholder = "Please enter a valid email account";
    input.required = true;
    input.id = "email";
    input.classList.add("form-control");
    input.removeAttribute("id");
    document.body.appendChild(input);
}