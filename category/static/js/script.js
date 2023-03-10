inputs = document.querySelectorAll('input , textarea');
for (var i = 0; i < inputs.length; i++) {
    inputs[i].classList.add('form-control');
}
labels = document.querySelectorAll('label');
for (var x = 0; x < labels.length; x++) {
    labels[x].classList.add('form-label text-danger');
}
spans = document.querySelectorAll('span');
for (var m = 0; m < spans.length; m++) {
    spans[m].classList.add('d-block');
}
select = document.querySelector('select')

select.classList.add('form-control')

divs = document.getElementsByClassName("form_element")
for (var d = 0; d < divs.length; d++) {
    divs[d].classList.add('mb-3')
}

checkboxex = document.querySelectorAll('input[type="checkbox"]')
for (var d = 0; d < checkboxex.length; d++) {
    checkboxex[d].classList.remove('form-control')
}