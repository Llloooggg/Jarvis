var a = 0;
function activeClass() {
    if (a == 0) {
        document.getElementById('dropdown').style.display = "block";
        a = 1;
    }
    else {
        document.getElementById('dropdown').style.display = "none";
        a = 0;
    }
}