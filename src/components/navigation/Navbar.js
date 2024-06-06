import { connect } from "react-redux";
import { Link } from "react-router-dom";

function Navbar(){
    return (
        <nav className="w-full py-6 top-0 transition duration-300 fixed ease-in-out z-50">  
            <div className="bg-white px-4 sm:px-6">
                {/*Have to be changed into img*/}
            <div className="-ml-4 -mt-2 flex flex-wrap items-center justify-between sm:flex-nowrap md:px-14">
                <div className="ml-4 mt-2">
                <h3 className="text-lg font-medium leading-6 text-gray-900">Flatner</h3>
                </div>
                <div className="ml-4 mt-2 flex-shrink-0">
                <Link to='/' className="text-lg inline-flex font-medium leading-6 text-gray-900 border-b-2 border-white hover:border-indigo-500 mx-4">Home</Link>
                <Link to='/busqueda' className="text-lg inline-flex font-medium leading-6 text-gray-900 border-b-2 border-white hover:border-indigo-500 mx-4">Search</Link>
                <Link to='/nosotros' className="text-lg inline-flex font-medium leading-6 text-gray-900 border-b-2 border-white hover:border-indigo-500 mx-4">About Us</Link>
                <Link to='/contacto' className="text-lg inline-flex font-medium leading-6 text-gray-900 border-b-2 border-white hover:border-indigo-500 mx-4">Contact</Link>
            <button
                type="button"
                className="ml-6 w-full sm:w-auto relative px-8 py-4 inline-flex items-center rounded-md border sm:px-6 sm:py-6 md:px-4 md:py-2 lg:px-3 lg:py-1 border-transparent bg-indigo-500 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
            >
                Login / Register
            </button>
        </div>
      </div>
    </div>
        </nav>
    )
}

const mapStateToProps = state => ({

})

export default connect(mapStateToProps,{
}) (Navbar);