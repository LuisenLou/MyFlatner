import Home from "containers/pages/Home";
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
            <Route path='*' element={<Error404/>}></Route>
            
            {/*Home display*/}
            <Route path='/' element={<Home/>}></Route>
            
          </Routes>
        </Router>
    </Provider>
   
  );
}

export default App;
