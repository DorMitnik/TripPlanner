
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
const ITINERARY_API_URL = process.env.REACT_APP_ITINERARY_URL || 'http://localhost:8001';

const api = axios.create({
  baseURL: API_BASE_URL,
});

const itineraryApi = axios.create({
  baseURL: ITINERARY_API_URL,
});

// Add token to requests
const addAuthInterceptor = (apiInstance) => {
  apiInstance.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  });
};

addAuthInterceptor(api);
addAuthInterceptor(itineraryApi);

export const authAPI = {
  login: (credentials) => api.post('/auth/login', credentials),
  register: (userData) => api.post('/auth/signup', userData),
};

export const tripsAPI = {
  getTrips: () => api.get('/trips'),
  createTrip: (tripData) => api.post('/trips', tripData),
  deleteTrip: (tripId) => api.delete('/trips', { params: { trip_id: tripId } }),
};

export const itineraryAPI = {
  generateItinerary: (tripId, userPrompt) => 
    itineraryApi.post(`/itinerary/generate-itinerary/${tripId}`, null, {
      params: { user_prompt: userPrompt }
    }),
};

export default api;
