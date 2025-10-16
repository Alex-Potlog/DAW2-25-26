const data1 = new Date();
const data2 = new Date();

function compareTo(d1, d2) {
    if (d1.getDate() === d2.getDate()) {
        return 0;
    }
    if (d1.getDate() < d2.getDate()) {
        return -1;
    }
    return 1;
}

console.log(compareTo(data1, data2));
