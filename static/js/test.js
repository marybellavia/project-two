var rental = "/api/rent_data";
var xField = 'Year';
var yField = 'Price';

var selectorOptions = {
    buttons: [{
        step: 'Year',
        stepmode: 'backward',
        count: 1,
        label: '1y'
    }, {
        step: 'year',
        stepmode: 'todate',
        count: 1,
        label: 'YTD'
    }],
};

Plotly.d3.json(rental, function(err, rentalData) {
    if(err) throw err;

    var data = prepData(rentalData);
    var layout = {
        title: 'Price Changes Over Time',
        xaxis: {
            rangeselector: selectorOptions,
            rangeslider: {}
        },
        yaxis: {
            fixedrange: true
        }
    };

    Plotly.plot("plot-irene", data, layout, {showSendToCloud: true});
});

function prepData(rentalData) {
    var x = [];
    var y = [];

    console.log(rentalData.length)

    rawData.forEach(function(datum, i) {
        if(i % 100) return;

        x.push(new Date(datum[xField]));
        y.push(datum[yField]);
    });

    return [{
        mode: 'lines',
        x: x,
        y: y
    }];
}