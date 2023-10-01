// Import necessary modules
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import CityList from './components/CityList';
import CityDetails from './components/CityDetails';
import LoginForm from './components/LoginForm';

function App() {
  return (
    <Router>
      <div>
        {/* Define routes */}
        <Switch>
          <Route path="/cities" component={CityList} />
          <Route path="/city/:id" component={CityDetails} />
          <Route path="/login" component={LoginForm} />
          {/* Add more routes as needed */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;
