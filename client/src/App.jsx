import { BrowserRouter, Routes, Route } from "react-router-dom"

import NavBar from './components/Navbar'
import HomePage from './pages/Home';
import SignUpPage from './pages/SignUp';
import LoginPage from './pages/Login';
import AllStocksPage from './pages/AllStocks';
import PortfolioPage from './pages/Portfolio';
import StockInfoPage from './pages/StockInfo';


export default function App() {
    return (
        <BrowserRouter>
            <NavBar />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/health" element={<h1>............IT WORKS............</h1>} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/signup" element={<SignUpPage />} />
                <Route path="/portfolio" element={<PortfolioPage />} />
                <Route path="/stocks" element={<AllStocksPage />} />
                <Route path="/stocks/:ticker" element={<StockInfoPage />} />
            </Routes>
        </BrowserRouter>
    )
}
