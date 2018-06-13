function logout() {
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open('DELETE', '/logout', true).send();
}

function showElem(id) {
    document.getElementById(id).style.visibility = "visible";
}

function closeElem(id) {
    document.getElementById(id).style.visibility = "hidden";
}