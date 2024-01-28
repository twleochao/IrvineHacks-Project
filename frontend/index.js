function initMap() {
    const map = new google.maps.Map(
      document.getElementById("map"),
      {
        zoom: 15,
        center: { lat: 33.6424, lng: -117.8417 },
      }
    );
    const geocoder = new google.maps.Geocoder();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const directionsService = new google.maps.DirectionsService();
  
    setPoints(map, tupleArray);
  }
  
  
  
  // function geocodeAddress(address) {    
  //         geocoder.geocode({ address }, (results, status) => {
  //         if (status === "OK") {
  //             const location = results[0].geometry.location;
  //             addTupleToArray([address, location.lat(), location.long()])
  //             // const marker = new google.maps.Marker({
  //             // map: map,
  //             // position: location,
  //             // title: address,
  //             // });
      
  //             // // Optionally, you can center the map on the geocoded location
  //             // map.setCenter(location);
  //         } else {
  //             // console.error(`Geocode was not successful for the following reason: ${status}`);
  //         }
  //         });
  //     }
  
  function setPoints(map, points) {
    for (let i = 0; i < points.length; i++) {
      const marker = points[i];
  
      new google.maps.Marker({
        position: { lat: marker[1], lng: marker[2] },
        map,
        title: marker[0],
      });
    }
  }
  
  let tupleArray = [];
  
  function addTupleToArray(tuple) {
    tupleArray.push(tuple);
  }
  
  function removeTuple(number) {
    tupleArray.splice(number, 1);
  }
  
  addTupleToArray(["uci", 33.6424, -117.84]);
  addTupleToArray(["test", 33.6424, -117.82]);
  
  // geocodeAddress("Student Center, G318, Bldg 204, Irvine, CA 92697");
  
  window.initMap = initMap;
  
  
  