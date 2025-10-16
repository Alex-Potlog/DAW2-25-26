const arr1 = ["", null, undefined, "Hola"];

for (let i = 0; i < arr1.length; i++) {
    if (arr1[i]) {
        console.log("Té contingut")
    } else if (arr1[i] == null) {
        console.log("És  null")
    } else if (arr1[i] == undefined) {
        console.log("És undefined")
    } else {
        console.log("No té contingut")
    }
}