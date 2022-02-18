window.addEventListener('load', function (e) {

    const card = document.querySelector('.form-container');


    const list = document.querySelector("#list");
    const input = document.querySelector("#new-todo");
    const btn = document.querySelector("#button-addon");

    //this function will allow us to check the clicked elements
    list.addEventListener('click', function (e) {
        if (e.target.tagName === 'LI') {
            e.target.classList.toggle('checked');
        }
    });

    // this function will allow us to add elements when we click the button
    btn.addEventListener('click', function () {
        const txt = input.value;
        if (input.value === '') {
            alert('you must write something');
        } else {
            const li = document.createElement('li');
            li.classList.add('p-3');
            li.classList.add('mb-4');
            li.classList.add('d-block');
            li.innerHTML = input.value.toString();

            list.insertBefore(li, list.childNodes[0]);
            input.value = '';
        }
    });

    card.classList.remove('hidden');

});