import social from '../../assets/img/chromicons/social.svg'
import services from '../../assets/img/chromicons/services.svg'
import security from '../../assets/img/chromicons/security.svg'
import filter from '../../assets/img/chromicons/filter.svg'
import phone from '../../assets/img/chromicons/phone.svg'



const incentives = [
    {
        name: 'Interacción Social',
        imageSrc: social,
        description: "Con nuestra aplicación, puedes interactuar con otros usuarios fácilmente. Comunícate con propietarios y posibles compañeros de piso para encontrar la mejor opción que se adapte a tus necesidades.",
    },
    {
        name: 'Servicios Adicionales: ',
        imageSrc: services,
        description: "Ofrecemos servicios adicionales útiles para hacer tu búsqueda más fácil. Desde asistencia en la búsqueda de compañeros de piso compatibles hasta ayuda con el proceso de mudanza, estamos aquí para ayudarte en cada paso del camino.",
    },
    {
        name: 'Seguridad y Confianza:',
        imageSrc: security,
        description: "Tu seguridad es nuestra prioridad. Implementamos medidas de seguridad robustas, incluyendo verificación de usuarios, evaluaciones y comentarios de otros usuarios, para garantizar una experiencia segura y confiable para todos.",
    },
    {
        name: 'Filtrado Avanzado:',
        imageSrc: filter,
        description: "Con nuestro sistema de filtrado avanzado, puedes personalizar tu búsqueda según tus preferencias específicas. Filtra por precio, ubicación, comodidades y más, para encontrar la habitación perfecta para ti.",
    },
    {
        name: 'Facilidad de Uso:',
        imageSrc: phone,
        description: "Nuestra aplicación es intuitiva y fácil de navegar. Con una interfaz de usuario sencilla y amigable, encontrarás lo que buscas en cuestión de minutos.",
    },
  ]

function Incentives() {
  return (
    <div className="bg-gradient-to-t from-emerald-100 to-white">
      <div className="mx-auto lg:mx-12 max-w-full sm:px-2 sm:py-32 lg:px-4">
        <div className="mx-auto max-w-2xl px-4 lg:max-w-none">
          <div className="max-w-3xl">
              <h2 className="text-4xl font-bold tracking-tight text-gray-900 mb-9">
                  Facilitamos la interacción entre personas.
              </h2>
              <p className="mt-4 text-gray-500">
                  En Flatner, estamos transformando la forma en que las personas encuentran y comparten espacios para vivir. Nos dedicamos a conectar propietarios de pisos con individuos que buscan habitaciones para compartir, ofreciendo una experiencia de búsqueda simple y eficiente.
              </p>
              <p className="mt-4 text-gray-500"> 
                  Con nuestra plataforma intuitiva, puedes explorar una amplia variedad de opciones de alojamiento en diferentes ubicaciones, desde apartamentos urbanos hasta acogedoras casas compartidas. Nuestro objetivo es hacer que el proceso de encontrar un compañero de piso sea fácil, seguro y sin complicaciones.
              </p>
              <p className="mt-4 text-gray-500"> 
                  Además de facilitar la búsqueda de alojamiento, en Flatner también ofrecemos servicios adicionales para hacer que la experiencia de vivir compartiendo sea aún más placentera. Desde asistencia en la búsqueda de compañeros de piso compatibles hasta ayuda con el proceso de mudanza, estamos aquí para ayudarte en cada paso del camino.
              </p>
              <p className="mt-4 text-gray-500">
                  Únete a nuestra comunidad en línea y descubre la comodidad y la emoción de vivir en un entorno compartido. ¡Empieza tu búsqueda hoy mismo en Flatner!
              </p>
          </div>
          <div className="mt-16 grid grid-cols-1 gap-y-10 gap-x-8 lg:grid-cols-3">
            {incentives.map((incentive) => (
              <div key={incentive.name} className="sm:flex lg:block">
                <div className="sm:flex-shrink-0">
                  <img className="h-16 w-16" src={incentive.imageSrc} alt="" />
                </div>
                <div className="mt-4 sm:mt-0 sm:ml-6 lg:mt-6 lg:ml-0">
                  <h3 className="text-sm font-medium text-gray-900">{incentive.name}</h3>
                  <p className="mt-2 text-sm text-gray-500">{incentive.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Incentives;