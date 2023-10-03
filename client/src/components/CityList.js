import React, { useState, useEffect } from 'react';

function CityList() {
  const [cities, setCities] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/cities')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch cities');
        }
        return response.json();
      })
      .then(data => setCities(data))
      .catch(error => {
        setError(error.message);
        console.error('Error fetching cities:', error);
      });
  }, []);

  return (
    <div>
      {error ? (
        <div>Error: {error}</div>
      ) : (
        <>
          <h1>List of Cities</h1>
          <ul>
            {cities.map(city => (
              <li key={city.id}>{city.name}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default CityList;

