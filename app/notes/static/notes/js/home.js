window.addEventListener('load', function(e) {
    const links = document.querySelectorAll('.home-link');

    // console.log(links);

    setTimeout(function() {
        links[0].classList.add('shown');
        links[0].classList.remove('hidden');
        links[1].classList.add('shown');
        links[1].classList.remove('hidden');
    }, 500);

});