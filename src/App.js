import { BrowserRouter as Router } from "react-router-dom";
import { Provider } from "react-redux";
import store from "./store";
import { Helmet, HelmetProvider } from 'react-helmet-async';
import AnimatedRoutes from './hocs/routes/routes'

function App() {
  
  return (
    <HelmetProvider>
      <Helmet>
        <title>Flatner | Room Partner App</title>
        <meta name='description' content='Contact with owners and other tenants at the easiest way'/>
        <meta name='keywords' content='pisos, habitaciones, propietario, inquilino'/>
        <meta name='author' content='LuisenLou'/>
        <meta name='publisher' content='Flatner'/>
        <meta name="robots" content='all' />
        <meta property="og:title" content='Flatner | Web' />
        <link rel='canonical' href='https://localhost:8000'/>
      </Helmet>
      <Provider store={store}>
          <Router>
            <AnimatedRoutes/>
          </Router>
      </Provider>
    </HelmetProvider>
    
   
  );
}

export default App;
