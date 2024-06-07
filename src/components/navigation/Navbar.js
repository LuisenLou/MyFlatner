import { connect } from "react-redux";
import { NavLink, Link } from "react-router-dom";
import ToggleMenu from './ToggleMenu'





function Navbar(){


    window.onscroll = function(){scrollFunction()}

    function scrollFunction(){
        if(document.getElementById('navbar')){
            if(document.body.scrollTop>50 || document.documentElement.scrollTop>50){
                document.getElementById('navbar').classList.add('shadow-navbar')
                document.getElementById('navbar').classList.add('bg-teal-700')
            }else{
                document.getElementById('navbar').classList.remove('shadow-navbar')
            }
        }
    }



    return (
        <nav id='navbar' className="w-full py-2 top-0 transition duration-300 bg-teal-700 fixed ease-in-out z-50">     
            <div className="px-12">
            <div className="flex items-center justify-between lg:flex md:flex ml-4 mt-2 pb-2 hidden">
                    <Link to='/' className="ml-4 mt-2">
                        <img
                            src={'https://tailwindui.com/img/logos/mark.svg?color=emerald&shade=600'}
                            alt='imagen'
                            width={40}
                            height={40}
                            className=""
                        />
                        <p>Flatner</p>
                    </Link>
                    <div className="ml-4 mt-2 flex-shrink-0">
                        <NavLink to='/' className="text-lg inline-flex font-medium leading-6 text-violet-50 border-b-2 border-white hover:border-emerald-500 mx-4">Home</NavLink>
                        <NavLink to='/busqueda' className="text-lg inline-flex font-medium leading-6 text-violet-50 border-b-2 border-white hover:border-emerald-500 mx-4">Search</NavLink>
                        <NavLink to='/nosotros' className="text-lg inline-flex font-medium leading-6 text-violet-50 border-b-2 border-white hover:border-emerald-500 mx-4">About Us</NavLink>
                        <NavLink to='/contacto' className="text-lg inline-flex font-medium leading-6 text-violet-50 border-b-2 border-white hover:border-emerald-500 mx-4">Contact</NavLink>
                        <Link to='/sesion'>
                            <button
                                className="ml-6 w-full sm:w-auto relative px-3 py-3 inline-flex items-center rounded-md border border-transparent bg-emerald-500 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2"
                            >
                                Login / Register
                            </button>
                        </Link>
                    </div>
                </div>
            </div>
            <div className="px-12 lg:hidden md:hidden flex flex-wrap items-center justify-between ">
                <Link to='/' className="ml-4 mt-2">
                <img
                    src={'https://tailwindui.com/img/logos/mark.svg?color=emerald&shade=600'}
                    alt='imagen'
                    width={40}
                    height={40}
                    className=""
                />
                </Link>
                <div className="flex-shrink-0">
                    <ToggleMenu/>
                </div>
            </div>
        </nav>
    )
}

const mapStateToProps = state => ({

})




export default connect(mapStateToProps,{
}) (Navbar);