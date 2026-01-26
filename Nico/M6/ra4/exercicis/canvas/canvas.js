const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const thumbContainer = document.getElementById('thumbContainer');


thumbContainer.addEventListener('click', function (e) {
    const thumbItem = e.target.closest('.thumb-item');

    if (thumbItem) {
        const imageSrc = thumbItem.getAttribute('data-src');
        loadImageToCanvas(imageSrc);
    }
});

function loadImageToCanvas(imageSrc) {
    const img = new Image();

    img.onload = function () {
        // Ajustar canvas: mida imatge + 10px per cada costat
        canvas.width = img.width + 20;
        canvas.height = img.height + 20;

        // Pintar fons verd
        ctx.fillStyle = 'green';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Dibuixar imatge amb 10px de marge
        ctx.drawImage(img, 10, 10);
    };

    img.src = imageSrc;
}