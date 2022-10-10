import 'bootstrap/dist/css/bootstrap.min.css'
import ReactDOM from 'react-dom'
import NavBar from './components/Navbar'
import { BrowserRouter, Routes, Route } from "react-router-dom"

import HomePage from './pages/Home';
import SignUpPage from './pages/SignUp';
import LoginPage from './pages/Login';
import AllStocksPage from './pages/AllStocks';
import PortfolioPage from './pages/Portfolio';
import StockInfoPage from './pages/StockInfo';


const App=()=>{
    return (
        <main className="container">
            <BrowserRouter>
            <NavBar/>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/signup" element={<SignUpPage />} />
                    <Route path="/portfolio" element={<PortfolioPage />} />
                    <Route path="/stocks" element={<AllStocksPage />} />
                    <Route path="/stocks/:ticker" element={<StockInfoPage />} />
                </Routes>
            </BrowserRouter>
        </main>
    )

}


ReactDOM.render(<App/>,document.getElementById('root'))