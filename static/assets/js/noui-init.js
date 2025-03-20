var rangeSlider = document.getElementById('slider-range');

noUiSlider.create(rangeSlider, {
    start: [250, 750],
    connect: true,
    range: {
        'min': [0],
        'max': [1000]
    }
});

var snapValues = [
    document.getElementById('range-min'),
    document.getElementById('range-max')
];

rangeSlider.noUiSlider.on('update', function (values, handle) {
    snapValues[handle].innerHTML = values[handle];
});
