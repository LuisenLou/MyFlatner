import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";

function Search(){

    return(
        <Layout>
            <Navbar/>
            <div className='pt-28'>
                Search
            </div>
            <Footer/>  
        </Layout>
    )
}
export default Search;