function GetCityName(){
    alert(document.getElementById('citySearchBox').value);
    document.getElementById('citySearchBox').value = "";
}

// Part 1
var trace1 = {
    x: ["beer", "wine", "martini", "margarita",
      "ice tea", "rum & coke", "mai tai", "gin & tonic"],
    y: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
    type: "bar"
  };
  
  var data = [trace1];
  
  var layout = {
    title: "'Bar' Chart"
  };
  
  Plotly.newPlot("plot-garrett", data, layout);