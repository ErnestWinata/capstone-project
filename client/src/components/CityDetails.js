import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function CityDetails() {
  const { id } = useParams(); 

  const [city, setCity] = useState(null);

  useEffect(() => {
    
    fetch(`http://localhost:5555/cities/${id}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch city details');
        }
        return response.json();
      })
      .then(data => setCity(data))
      .catch(error => console.error('Error fetching city details:', error));
  }, [id]);

  return (
    <div>
      {city ? (
        <div>
          <h1>{city.name}</h1>
          <p>Date of Visit: {city.date_of_visit}</p>
          <p>Best Memories: {city.best_memories}</p>
          <p>Accommodation: {city.accommodation}</p>
        </div>
      ) : (
        <div>Loading city details...</div>
      )}
    </div>
  );
}

export default CityDetails;