import React from 'react';
import './search.css';

const Search = () => {
  // Example list of suggestions
  const suggestions = ["Event 1", "Event 2", "Event 3", "Conference", "Concert"];

  return (
    <div className="search-container">
      <div className="blank-section"></div>
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
