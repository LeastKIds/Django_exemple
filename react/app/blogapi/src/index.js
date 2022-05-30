import React from 'react';
// import ReactDOM from 'react-dom';
import * as ReactDOM from 'react-dom/client';
import './index.css';
import {Route, BrowserRouter as Router, Routes} from "react-router-dom";
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';
import reportWebVitals from "./reportWebVitals";

const routing = (

    <Router>
        <React.StrictMode>
            <Header/>
            <Routes>
                <Route exact path="/" element={<App/>}/>
            </Routes>
            {/*<Footer />*/}
        </React.StrictMode>
    </Router>
)

// ReactDOM.render(routing, document.getElementById('root'));
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(routing);

reportWebVitals(console.log);