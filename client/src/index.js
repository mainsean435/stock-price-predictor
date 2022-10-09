import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css'
import ReactDOM from 'react-dom'
import NavBar from './components/Navbar';
import { BrowserRouter, Routes, Route } from "react-router-dom"

import HomePage from './components/Home';
import SignUpPage from './components/SignUp';
import LoginPage from './pages/Login';
import AllStocksPage from './pages/AllStocks';
import MyWatchlistPage from './components/MyWatchlist';
import StockInfoPage from './components/StockInfo';


const App=()=>{
    return (
        <main className="container">
            <BrowserRouter>
            <NavBar/>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/signup" element={<SignUpPage />} />
                    <Route path="/my-watchlist" element={<MyWatchlistPage />} />
                    <Route path="/all-stocks" element={<AllStocksPage />} />
                    <Route path="/stock/:ticker" element={<StockInfoPage title="Stock price"/>} />
                </Routes>
            </BrowserRouter>
        </main>
    )

}


ReactDOM.render(<App/>,document.getElementById('root'))