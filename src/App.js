import Home from "containers/pages/Home";
import Search from "containers/pages/Search";
import AboutUs from "containers/pages/AboutUs";
import Communicate from "containers/pages/Communicate";
import Sign from 'containers/pages/Sign'
import Error404 from "containers/error/Error404";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Provider } from "react-redux";
import store from "store";


function App() {
  return (

    <Provider store={store}>
        <Router>
          <Routes>
            {/*Error display*/}
            <Route path='*' element={<Error404/>}/>
            
            {/*Pages display*/}
            <Route path='/' element={<Home/>}/>
            <Route path='/busqueda' element={<Search/>}/>
            <Route path='/nosotros' element={<AboutUs/>}/>
            <Route path='/contacto' element={<Communicate/>}/>

            {/*Sesion display*/}
            <Route path='/sesion' element={<Sign/>}/>
            
            
          </Routes>
        </Router>
    </Provider>
   
  );
}

export default App;
