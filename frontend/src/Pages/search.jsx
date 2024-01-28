import React from 'react';
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
  const suggestions = ["Event 1", "Event 2", "Event 3", "Conference", "Concert"];

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
          list="eventSuggestions"
        />
        <datalist id="eventSuggestions">
          {suggestions.map((item, index) => (
            <option key={index} value={item} />
          ))}
        </datalist>
        <button>SEARCH</button>
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
