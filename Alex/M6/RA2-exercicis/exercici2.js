const title = ['La casa de paper', 'La catedral del mar', 'Panegre', 'Polseres vermelles'];
for (let i = 0; i < title.length; i++) {
    title[i] = title[i].replaceAll(' ', '-');
    title[i] = title[i].toLowerCase();
}
title.forEach(title => console.log(title));