const form = document.createElement('form');
form.action = '#';
form.method = 'POST';
form.id = 'user-data';
form.name = "user-data";

const email = document.createElement('input');
email.type = 'email';
email.name = 'email';
email.placeholder = 'Enter your email';
email.required = true;

const boto = document.createElement('button');
boto.type = 'submit';
boto.id = 'send';

form.appendChild(email);
form.appendChild(boto);

document.body.appendChild(form);