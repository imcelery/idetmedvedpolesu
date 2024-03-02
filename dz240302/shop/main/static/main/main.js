window.addEventListener("load", () => {
    const Http = new XMLHttpRequest();
    const url = '/api/get_goods';
    Http.open("GET", url);
    Http.responseType = 'json';

    Http.onload = (e) => {
        const good = document.getElementByClassName('good-list')[0];

        Http.response.forEach(($li) => {
            const newSpan = document.createElement("dir");
            const newContent = document.createTextNode($li);
            newSpan.appendChild(newContent);
            good.appendChild(newSpan);

        });
    };
    Http.send();
});