// Creating map object
var myMap = L.map("map", {
    center: [37.09024, -95.712891],
    zoom: 5
  });
  
  // Adding tile layer to the map
  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  }).addTo(myMap);
  
  // Store API query variables
  var baseURL = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?";
  // Add the dates in the ISO formats
  var date = "$where=created_date between '2016-01-01T00:00:00' and '2017-01-01T00:00:00'";
  // Add the complaint type
  var complaint1 = "&complaint_type=Illegal Animal Kept as Pet";
  var complaint2 = "&complaint_type=Animal Abuse";
  // Add a limit
  var limit = "&$limit=10000";
  
  // Assemble API query URL
  var url1 = baseURL + date + complaint1 + limit;
  var url2 = baseURL + date + complaint2 + limit;
  console.log(url2);
  
  d3.json(url2, function(response) {
    console.log(response);
    var heatArray = [];
    for (var i = 0; i < response.length; i++) {
      var location = response[i].location;
      if (location) {
        heatArray.push([location.coordinates[1], location.coordinates[0]]);
      }
    }
    var heat = L.heatLayer(heatArray, {
      radius: 25,
      blur: 35
    }).addTo(myMap);
  
  });