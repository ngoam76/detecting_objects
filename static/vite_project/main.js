function show(){
    document.querySelector('.hamburger').classList.toggle('open');
    document.querySelector('.navigation-left').classList.toggle('active');
}


function showright(){
    document.querySelector('.plus').classList.toggle('open');
    document.querySelector('.navigation-right').classList.toggle('active');
}

const weight = document.getElementById('weight')
const weightRangeValue = document.getElementById('weight-range-value');
weight.addEventListener('input', function(){
    weightRangeValue.textContent = weight.value;
})

const zoom = document.getElementById('zoom');
const zoomRangeValue = document.getElementById('zoom-range-value');
zoom.addEventListener('input', function(){
    zoomRangeValue.textContent = zoom.value;
})