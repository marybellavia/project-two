function GetCityName(){
    alert(document.getElementById('citySearchBox').value);
    document.getElementById('citySearchBox').value = "";
}

var red = 'rgb(255, 48, 37)';
var green = 'rgb(42, 233, 69)';
var trace1 = {
    x: [1, 1, 1, 1],
    y: [70000, 125000, 310000, 700000],
    mode: 'markers',
    marker: {
      size: [3, 10, 20, 60],
      color: [red, green, red, green],
      opacity: [0.4, 0.4, 0.4, 0.4],
    }
  };
  
  var data = [trace1];
  
  var layout = {
    showline: false,
    title: 'House Price 2014 vs. 2021',
    showlegend: false,
    height: 800,
    width: 800
  };
  
  Plotly.newPlot("plot-garrett", data, layout);