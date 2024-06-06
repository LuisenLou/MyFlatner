import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";

function AboutUs(){

    return(
        <Layout>
            <Navbar/>
            <div className='pt-28 pb-28'>
                <div className="items-center justify-center">
                    <div className="text-black-500 px-20 mx-20">
                        <p className="mt-4">Bienvenido a nuestra aplicación, donde la conexión entre propietarios e inquilinos se convierte en la clave para una experiencia de convivencia enriquecedora y confiable. Creemos firmemente en los beneficios de una comunidad bien conectada, donde todos se sientan valorados y apoyados.</p>
                    </div>
                    <div className="text-black-500 px-20 mx-20">
                        <p className="mt-4 text-black-500">Para los propietarios, nuestra aplicación ofrece una plataforma segura y conveniente para interactuar con sus inquilinos. Desde la comunicación sobre reparaciones y mantenimiento hasta la gestión de pagos de alquiler, estamos aquí para facilitar cada paso del proceso. Al fomentar una relación abierta y transparente, ayudamos a construir una base sólida de confianza mutua entre propietarios e inquilinos.</p>
                    </div>
                    <div className="text-black-500 px-20 mx-20">
                        <p className="mt-4 text-black-500">Pero nuestra aplicación no se detiene ahí. Reconocemos la importancia de conectar a los inquilinos entre sí para fomentar un sentido de comunidad y colaboración. Con funciones que facilitan la comunicación y la organización de eventos comunitarios, creamos un entorno donde los inquilinos pueden conocerse, compartir intereses y apoyarse mutuamente.</p>
                    </div>
                    <div className="text-black-500 px-20 mx-20">
                        <p className="mt-4 text-black-500">Al promover una cultura de respeto, empatía y cooperación, nuestra aplicación no solo mejora la experiencia de convivencia, sino que también contribuye a un ambiente más armonioso y positivo para todos. Únete a nuestra comunidad hoy y descubre cómo la conexión puede transformar tu experiencia de vida compartida. ¡Te damos la bienvenida a un mundo de confianza y coliving mejorado!</p>
                    </div>
                </div>
            </div>
            <Footer/>  
        </Layout>
    )
}
export default AboutUs;