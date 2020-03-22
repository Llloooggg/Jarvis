var a = 0;
//  orange = "#c77814";
//  gray ="#b9b9b9";

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

document.addEventListener('click', function(e) {
    if (e.target.className === 'contacts__schedule') {
      e.target.style.color = e.target.style.color === 'gray' ? 'orange' : 'gray';
    }
  });




$(function() {
    setTimeout(function() {
         $('#1').show(400);
    }, 500);
    setTimeout(function() {
        $('#1').hide(400);
    }, 6000);
  });