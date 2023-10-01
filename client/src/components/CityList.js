import React, { useState, useEffect } from 'react';

function CityList() {
  const [cities, setCities] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/cities')  // Replace with your API URL
      .then(response => response.json())
      .then(data => setCities(data))
      .catch(error => console.error('Error fetching cities:', error));
  }, []);

  return (
    <div>
      <h1>List of Cities</h1>
      <ul>
        {cities.map(city => (
          <li key={city.id}>{city.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default CityList;

