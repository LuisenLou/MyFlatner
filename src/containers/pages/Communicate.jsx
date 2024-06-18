import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";
import { useState } from "react";
import { connect } from "react-redux";
import { submitForm } from "redux/actions/contact_form/form";


function Communicate({
    submitForm,
}
){
    /*const [agreed, setAgreed] = useState(false)*/

    const [formData, setFormData] = useState({
        reason:'',
        first_name:'',
        last_name:'',
        email:'',
        country:'',
        city:'',
        region:'',
        via:'',
        address_name:'',
        postal_code:'',
        description:'',
    });

    const{
        reason,
        first_name, 
        last_name, 
        email, 
        country,
        city, 
        region,
        via,
        address_name,
        postal_code,
        description} = formData;

        const onChangeData = e => setFormData({...formData,[e.target.name]:e.target.value})

        const onSubmit = e =>{
            e.preventDefault()
            submitForm(formData)
        }

        const onDelete = e => setFormData({
            reason:'',
            first_name:'',
            last_name:'',
            email:'',
            country:'',
            city:'',
            region:'',
            address_name:'',
            postal_code:'',
            description:'',
        })


    return(
        <Layout>
            <Navbar/>
            <div className='pt-28 bg-gradient-to-b from-emerald-100 to-white'>
                <form onSubmit={e => {onSubmit(e)}}>
                    <div className="space-y-12 mx-auto max-w-4xl items-center sm:py-10 lg:py-2 px-8 bg-gradient-to-b from-emerald-100 to-white">
                        <div className="border-b border-gray-900/10 pb-12">
                            <div className="border-b border-gray-900/10 pb-12">
                                <h2 className="text-base font-semibold leading-7 text-gray-900">La siguiente información proporcionada se usará con fines al uso requerido por el solicitante.</h2>
                                    <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-4">
                                        <div className="sm:col-span-3">
                                            <label htmlFor="reason" className="block text-sm font-medium leading-6 text-gray-900">
                                                Motivo*
                                            </label>
                                                <div className="mt-2">
                                                    <select
                                                    id="reason"
                                                    name="reason"
                                                    value={reason}
                                                    required
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    >
                                                        <option></option>
                                                        <option>Sugerencia</option>
                                                        <option>Duda</option>
                                                        <option>Petición</option>
                                                        <option>Opinion</option>
                                                    </select>
                                                </div>
                                        </div>
                                        
                                        
                                        <div className="sm:col-span-3">
                                            <label htmlFor="first_name" className="block text-sm font-medium leading-6 text-gray-900">
                                                Nombre*
                                            </label>
                                                <div className="mt-2">
                                                    <input
                                                    type="text"
                                                    name="first_name"
                                                    value={first_name}
                                                    id="first_name"
                                                    required
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                        </div>

                                        <div className="sm:col-span-3">
                                            <label htmlFor="last_name" className="block text-sm font-medium leading-6 text-gray-900">
                                                Apellido*
                                            </label>
                                                <div className="mt-2">
                                                    <input
                                                    type="text"
                                                    name="last_name"
                                                    value={last_name}
                                                    id="last_name"
                                                    required
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                        </div>

                                        <div className="sm:col-span-4">
                                            <label htmlFor="email" className="block text-sm font-medium leading-6 text-gray-900">
                                                Correo Electrónico*
                                            </label>
                                                <div className="mt-2">
                                                    <input
                                                    id="email"
                                                    name="email"
                                                    value={email}
                                                    type="email"
                                                    autoComplete="email"
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                        </div>

                                        <div className="sm:col-span-3">
                                            <label htmlFor="country" className="block text-sm font-medium leading-6 text-gray-900">
                                                País*
                                            </label>
                                                <div className="mt-2">
                                                    <select
                                                    id="country"
                                                    name="country"
                                                    value={country}
                                                    required
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    >
                                                        <option></option>
                                                        <option>España</option>
                                                        <option>Portugal</option>
                                                        <option>Francia</option>
                                                        <option>Alemania</option>
                                                        <option>Inglaterra</option>
                                                        <option>Italia</option>
                                                    </select>
                                                </div>
                                        </div>

                                        <div className="sm:col-span-2 sm:col-start-1">
                                            <label htmlFor="city" className="block text-sm font-medium leading-6 text-gray-900">
                                                Ciudad
                                            </label>
                                                <div className="mt-2">
                                                    <input
                                                    type="text"
                                                    name="city"
                                                    value={city}
                                                    id="city"
                                                    autoComplete="address-level2"
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                        </div>

                                        <div className="sm:col-span-2">
                                            <label htmlFor="region" className="block text-sm font-medium leading-6 text-gray-900">
                                                Estado / Provincia
                                            </label>
                                                <div className="mt-2">
                                                    <input
                                                    type="text"
                                                    name="region"
                                                    value={region}
                                                    id="region"
                                                    autoComplete="address-level1"
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                        </div>

                                        <div className="col-span-full inline-flex">
                                            <div className="sm:col-span-1 sm:col-start-1 mr-2">
                                                <label htmlFor="via" className="block text-sm font-medium leading-6 text-gray-900">
                                                    Vía
                                                </label>
                                                <div className="my-2">
                                                    <select
                                                    id="via"
                                                    name="via"
                                                    value={via}
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:max-w-xs sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    >
                                                        <option></option>
                                                        <option>Calle</option>
                                                        <option>Avenida</option>
                                                        <option>Plaza</option>
                                                        <option>Carretera</option>
                                                        <option>Paseo</option>
                                                        <option>Ronda</option>
                                                    </select>
                                                </div>
                                            </div>
                                            <div className="col-span-3">
                                                <label htmlFor="address_name" className="block text-sm font-medium leading-6 text-gray-900">
                                                    Nombre
                                                </label>
                                                <div className="mt-2">
                                                    <input
                                                    type="text"
                                                    name="address_name"
                                                    value={address_name}
                                                    id="address_name"
                                                    autoComplete="address_name"
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                            </div>
                                        </div>

                                        <div className="sm:col-span-2">
                                            <label htmlFor="postal_code" className="block text-sm font-medium leading-6 text-gray-900">
                                                Código Postal
                                            </label>
                                                <div className="mt-2">
                                                    <input
                                                    type="text"
                                                    name="postal_code"
                                                    value={postal_code}
                                                    id="postal_code"
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                        </div>
                                        <div className="col-span-full">
                                            <label htmlFor="description" className="block text-sm font-medium leading-6 text-gray-900">
                                                Descripción*
                                            </label>
                                                <div className="mt-2">
                                                    <textarea
                                                    id="description"
                                                    name="description"
                                                    value={description}
                                                    required
                                                    rows={3}
                                                    className="block w-full rounded-md bg-gray-50 border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-emerald-600 sm:text-sm sm:leading-6"
                                                    onChange={e=>onChangeData(e)}
                                                    />
                                                </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="w-full text-center my-2">
                                    <span className='inline-block'> Campos marcados con (*) son obligatorios </span>
                                </div>
                                <div className="my-10 flex items-center justify-center gap-x-6">
                                    <button 
                                        onClick={e=>onDelete(e)}
                                        type="button" 
                                        className="rounded-md bg-gray-200 px-3 py-3 text-sm font-semibold leading-6 text-gray-900 shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600"
                                    >
                                    Borrar
                                    </button>
                                    <button
                                        type="submit"
                                        className="rounded-md bg-emerald-600 px-4 py-3 text-sm font-semibold text-white shadow-sm hover:bg-emerald-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-emerald-600"
                                    >
                                    Enviar
                                    </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
            <Footer/>  
        </Layout>
    )
}

const mapStateToProps=state=>({
    

})

export default connect(mapStateToProps,{
    submitForm

})(Communicate);






