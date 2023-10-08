
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import CityList from './components/CityList';
import { Formik } from 'formik'
import CityDetails from './components/CityDetails';
import LoginForm from './components/LoginForm';

function App() {
  return (
    <Router>
      <div>
        
        <Switch>
          <Route path="/cities" component={CityList} />
          {/* <Route path="/city/:id" component={CityDetails} /> */}
          <Route path="/login" component={LoginForm} />
          
        </Switch>
      </div>
    </Router>
  );
}

export default App;
