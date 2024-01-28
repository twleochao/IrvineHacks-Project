let currentLocation;

let directionsRenderer;
let directionsService;

function initMap() {
  const map = new google.maps.Map(
    document.getElementById("map"),
    {
      zoom: 15,
      center: { lat: 33.6424, lng: -117.8417 },
    }
  );
  directionsRenderer = new google.maps.DirectionsRenderer();
  directionsRenderer.setMap(map);
  directionsService = new google.maps.DirectionsService();
  

  const origin = new google.maps.LatLng(33.6424, -117.84); // Replace with your actual origin coordinates
//   const destination = new google.maps.LatLng(34.6424, -117.82); // Replace with your actual destination coordinates

  const infoWindow = new google.maps.InfoWindow();

  setPoints(map, tupleArray);

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
          let pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };

        currentLocation = [pos.lat, pos.lng];
        calculateAndDisplayRoute(currentLocation, tupleArray[0]);

        // infoWindow.setPosition(pos);
        // infoWindow.setContent("Location found.");
        // infoWindow.open(map);
        // map.setCenter(pos);

        // new google.maps.Marker({
        //   position: pos,
        //   map,
        //   icon: {
        //     path: google.maps.SymbolPath.CIRCLE,
        //     scale: 10,
        //     fillColor: "#0000FF",
        //     fillOpacity: 1,
        //     strokeWeight: 2,
        //     strokeColor: "#000000",
        //   },
        // //   title: "Your Location",
        // });
      },
      () => {

        handleLocationError(true, infoWindow, map.getCenter());
      },
    );
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }


//   if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(
//       (position) => {
//         const userLocation = {
//           lat: position.coords.latitude,
//           lng: position.coords.longitude,
//         };

//         infoWindow.setPosition(pos);
//         infoWindow.setContent("Loation found.");
//         infoWindow.open(map);
//         map.setCenter(pos);
//         // new google.maps.Marker({
//         //   position: userLocation,
//         //   map,
//         //   visible: true,
//         //   title: "Your Location",
//         // });
//       },
//       (error) => {
//         console.error("Error getting user location:", error.message);
//       }
//     );
//   } else {
//     console.error("Geolocation is not supported by this browser.");
//   }
// 33.6424, -117.82
// const pos = { 33.6424, -117.82};
// 33.6424, -117.84
// 33.6424, -117.82

// const destination1 = {lat: 33.6424, lng: -117.84};
// const destination2 = { lat: 33.6424, lng: -117.82 };
const destination3 = [33.6424, -117.84];
const destination4 = [33.6424, -117.82];

// console.log(currentLocation[0])
// calculateAndDisplayRoute(currentLocation, destination4);
}


function setPoints(map, points) {
  for (let i = 0; i < points.length; i++) {
    const marker = points[i];

    // new google.maps.Marker({
    //   position: { lat: marker[0], lng: marker[1] },
    //   map,
    // //   title: marker[0],
    // });
  }
}

let tupleArray = [];

function addTupleToArray(tuple) {
  tupleArray.push(tuple);
}

function removeTuple(number) {
  tupleArray.splice(number, 1);
}

addTupleToArray([33.6424, -117.80]);



function calculateAndDisplayRoute(start, end) {
    const request = {
        origin: {lat: start[0], lng: start[1]},
        destination: {lat: end[0], lng: end[1]},
        travelMode: google.maps.TravelMode.DRIVING,
      };
    // const request = {
    //   origin: start,
    //   destination: end,
    //   travelMode: google.maps.TravelMode.DRIVING,
    // };
  
    directionsService.route(request, (result, status) => {
      if (status == google.maps.DirectionsStatus.OK) {
        directionsRenderer.setDirections(result);
      } else {
        console.error("Directions request failed:", status);
      }
    });
  }

// if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(
//       (position) => {
//         const userLocation = {
//           lat: position.coords.latitude,
//           lng: position.coords.longitude,
//         };

//         // Display the user's location on the map
//         map.setCenter(userLocation);
//         map.setZoom(15);

//         new google.maps.Marker({
//           position: userLocation,
//           map,
//           title: "Your Location",
//         });
//       },
//       (error) => {
//         console.error("Error getting user location:", error.message);
//       }
//     );
//   } else {
//     console.error("Geolocation is not supported by this browser.");
//   }


window.initMap = initMap;





