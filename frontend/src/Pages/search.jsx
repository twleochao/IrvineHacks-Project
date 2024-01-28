import React, { useState } from 'react';
import eventData from "./fnl.json";
// import React, {useState} from 'react';

console.log(eventData)

// const fs = require('fs');

// // Specify the path to your JSON file
// const filePath = 'IrvineHacks-Project/fnl.json';

// // Read the JSON file
// fs.readFile(filePath, 'utf-8', (err, data) => {
//   if (err) {
//     console.error('Error reading JSON file:', err);
//     return;
//   }

//   // Parse the JSON data
//   const jsonData = JSON.parse(data);
//   jsonData.forEach(i => {
//     console.log('Name:', i.name);
//     console.log('Imgsrc:', i.imgsrc);
//     console.log('Time:', i.time);
//     console.log('Location:', i.loc);
//     console.log('Address:', i.add);
//     console.log('Coordinates:', i.cords);
//   })

// });



// import {GoogleMap, useJsApiLoader } from '@react-google-maps/api';
// import './search.css';

// const containerStyle = {
//   width: '400px',
//   height: '400px'
// };

// const center = {
//   lat: -3.745,
//   lng: -38.523
// };

// function MyComponent() {
//   const { isLoaded } = useJsApiLoader({
//     id: 'google-map-script',
//     googleMapsApiKey: "AIzaSyA3eqFuwarzFiN4CIY4hkKBMpyxWTYgyRM"
//   })

//   const [map, setMap] = React.useState(null)

//   const onLoad = React.useCallback(function callback(map) {
//     // This is just an example of getting and using the map instance!!! don't just blindly copy!
//     const bounds = new window.google.maps.LatLngBounds(center);
//     map.fitBounds(bounds);

//     setMap(map)
//   }, [])

//   const onUnmount = React.useCallback(function callback(map) {
//     setMap(null)
//   }, [])

//   return isLoaded ? (
//       <GoogleMap
//         mapContainerStyle={containerStyle}
//         center={center}
//         zoom={10}
//         onLoad={onLoad}
//         onUnmount={onUnmount}
//       >
//         { /* Child components, such as markers, info windows, etc. */ }
//         <></>
//       </GoogleMap>
//   ) : <></>
// }

const Search = () => {
  // Example list of suggestions
  const suggestions = []
  for(let i = 0; i < eventData.length; i++){
    suggestions.push(eventData[i].name)
  }

  const [userInput, setUserInput] = useState('');

  const handleInputChange = (event) => {
    setUserInput(event.target.value);
  }

  const handleButtonClick = () => {
    console.log('User input:', userInput);
  }

  
  return (
    <div className="search-container">

      <link rel="stylesheet" type="text/css" href="./../style.css" />
      <script type="module" src="./../index.js"></script>

      <div className="blank-section"></div>

      <div id="map"></div>

      <script
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyA3eqFuwarzFiN4CIY4hkKBMpyxWTYgyRM&callback=initMap&v=weekly"
      defer
      ></script>

      <div className="search-section">
        <h2>SEARCH BAR</h2>
        <input
          type="text"
          placeholder="FIND AN EVENT"
          value = {userInput}
          list="eventSuggestions"
        />
        <datalist id="eventSuggestions">
          {suggestions.map((item, index) => (
            <option key={index} value={item} />
          ))}
        </datalist>
        <button onClick={handleButtonClick}>SEARCH</button>
        <div className="additional-info">
          <div className="info-item">
            <div>
              
              <span>Time:</span> Your Time Goes Here
            </div>
            <div>
              <span>Address:</span> Your Address Goes Here
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Search;
// export default React.memo(MyComponent)
