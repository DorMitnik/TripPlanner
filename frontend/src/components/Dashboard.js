
import React, { useState, useEffect } from 'react';
import { tripsAPI, itineraryAPI } from '../services/api';

const Dashboard = ({ token, logout }) => {
  const [trips, setTrips] = useState([]);
  const [showAddTrip, setShowAddTrip] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [newTrip, setNewTrip] = useState({
    destination: '',
    start_date: '',
    end_date: ''
  });
  const [itineraryPrompt, setItineraryPrompt] = useState('');
  const [generatedItinerary, setGeneratedItinerary] = useState('');
  const [selectedTripId, setSelectedTripId] = useState(null);

  useEffect(() => {
    fetchTrips();
  }, []);

  const fetchTrips = async () => {
    try {
      const response = await tripsAPI.getTrips();
      setTrips(response.data);
    } catch (err) {
      setError('Failed to fetch trips');
    }
  };

  const handleAddTrip = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      await tripsAPI.createTrip(newTrip);
      setSuccess('Trip added successfully!');
      setNewTrip({ destination: '', start_date: '', end_date: '' });
      setShowAddTrip(false);
      fetchTrips();
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to add trip');
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteTrip = async (tripId) => {
    if (window.confirm('Are you sure you want to delete this trip?')) {
      try {
        await tripsAPI.deleteTrip(tripId);
        setSuccess('Trip deleted successfully!');
        fetchTrips();
      } catch (err) {
        setError('Failed to delete trip');
      }
    }
  };

  const handleGenerateItinerary = async (tripId) => {
    if (!itineraryPrompt.trim()) {
      setError('Please enter a prompt for itinerary generation');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await itineraryAPI.generateItinerary(tripId, itineraryPrompt);
      setGeneratedItinerary(response.data);
      setSelectedTripId(tripId);
      setSuccess('Itinerary generated successfully!');
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to generate itinerary');
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    setNewTrip({
      ...newTrip,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="container">
      <div className="header">
        <h1>Trip Planner Dashboard</h1>
        <button onClick={logout} className="btn btn-secondary">
          Logout
        </button>
      </div>

      {error && <div className="error">{error}</div>}
      {success && <div className="success">{success}</div>}

      <div style={{ marginBottom: '20px' }}>
        <button 
          onClick={() => setShowAddTrip(!showAddTrip)} 
          className="btn btn-primary"
        >
          {showAddTrip ? 'Cancel' : 'Add New Trip'}
        </button>
      </div>

      {showAddTrip && (
        <div className="form-container">
          <h3>Add New Trip</h3>
          <form onSubmit={handleAddTrip}>
            <div className="form-group">
              <label htmlFor="destination">Destination:</label>
              <input
                type="text"
                id="destination"
                name="destination"
                value={newTrip.destination}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="start_date">Start Date:</label>
              <input
                type="datetime-local"
                id="start_date"
                name="start_date"
                value={newTrip.start_date}
                onChange={handleInputChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="end_date">End Date:</label>
              <input
                type="datetime-local"
                id="end_date"
                name="end_date"
                value={newTrip.end_date}
                onChange={handleInputChange}
                required
              />
            </div>
            <button type="submit" className="btn btn-primary" disabled={loading}>
              {loading ? 'Adding...' : 'Add Trip'}
            </button>
          </form>
        </div>
      )}

      <div>
        <h2>Your Trips</h2>
        {trips.length === 0 ? (
          <p>No trips found. Add your first trip!</p>
        ) : (
          trips.map((trip) => (
            <div key={trip.id} className="trip-card">
              <h3>{trip.destination}</h3>
              <p>
                <strong>Start:</strong> {new Date(trip.start_date).toLocaleDateString()} <br />
                <strong>End:</strong> {new Date(trip.end_date).toLocaleDateString()}
              </p>
              <div style={{ marginTop: '15px' }}>
                <input
                  type="text"
                  placeholder="Enter prompt for itinerary generation..."
                  value={itineraryPrompt}
                  onChange={(e) => setItineraryPrompt(e.target.value)}
                  style={{ width: '300px', marginRight: '10px' }}
                />
                <button
                  onClick={() => handleGenerateItinerary(trip.id)}
                  className="btn btn-primary"
                  disabled={loading}
                >
                  {loading ? 'Generating...' : 'Generate Itinerary'}
                </button>
                <button
                  onClick={() => handleDeleteTrip(trip.id)}
                  className="btn btn-danger"
                >
                  Delete Trip
                </button>
              </div>

              {selectedTripId === trip.id && generatedItinerary && (
                <div className="itinerary">
                  <h4>Generated Itinerary:</h4>
                  <pre>{generatedItinerary}</pre>
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Dashboard;
