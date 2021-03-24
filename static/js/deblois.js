function GetCityName(){
    alert(document.getElementById('citySearchBox').value);
    document.getElementById('citySearchBox').value = "";
}

var red = 'rgb(255, 48, 37)';
var green = 'rgb(42, 233, 69)';
var cityX = Array.from({length: 4}, (x, i) => i+1); //number of cities in the house data set (893 cities will be final number)

var trace1 = {
    x: cityX,
    y: [70000, 125000, 310000, 700000], //house sell price
    text: ['City: St. Louis<br>Avg House Price 2021: $70,000<br>Amount Change: $-3,000', 'City: Austin<br>Avg House Price 2021: $125,000<br>Amount Change: $10,000', 'City: San Francisco<br>Avg House Price 2021: $310,000<br>Amount Change: $-20,000', 'City: New York City<br>Avg House Price 2021: $700,000<br>Amount Change: $60,000'],
    mode: 'markers',
    marker: {
      size: [3, 10, 20, 60], //relative price change for 2014 vs 2020
      color: [red, green, red, green],
      opacity: [0.4, 0.4, 0.4, 0.4] //see if i can set all points to the same opacity
    }
  };
  
  var data = [trace1];
  
  var layout = {
    title: 'House Price 2014 vs. 2021',
    showlegend: false,
    height: 800,
    width: 800
  };
  
  Plotly.newPlot("plot-garrett", data, layout);