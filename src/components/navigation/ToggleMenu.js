import { useState } from "react";
import { NavLink } from "react-router-dom";

function ToggleMenu() {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
      setIsOpen(!isOpen);
      isOpen === false 
      ? document.getElementById('toggle').classList.add('p-6','rounded', 'mr-4', 'border') 
      : document.getElementById('toggle').classList.remove('p-6')

    };

  return (
    <nav id='toggle' className="absolute right-0 top-4 mr-4 flex items-center justify-between flex-wrap bg-teal-900">
      <div className="block lg:hidden right-0 top-4 mr-4 fixed">
        <button 
          className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white"
          onClick={toggleMenu}
        >
          <svg className="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <title>Menú móvil</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
          </svg>
        </button>
      </div>
      <div className={`w-full block flex-grow lg:flex lg:items-center lg:w-auto ${isOpen ? '' : 'hidden'}`}>
        <div className="text-sm lg:flex-grow">
          <NavLink to='/' className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
            Inicio
          </NavLink>
          <NavLink to='/busqueda' className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
            Search
          </NavLink>
          <NavLink to='/nosotros' className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
            Nosotros
          </NavLink>
          <NavLink to='/contacto' className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
            Contacto
          </NavLink>
          <button>
            <NavLink to='/sesion' className="w-full sm:w-auto relative px-2 py-2 mt-3 inline-flex items-center rounded-md border border-transparent bg-emerald-500 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2">
              Inicio/Registro
            </NavLink>
          </button>
        </div>
      </div>
    </nav>
  );
}

export default ToggleMenu;
