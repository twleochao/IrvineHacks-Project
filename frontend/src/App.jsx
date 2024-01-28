import { useState } from "react"
import Background from "./Components/Background/Background";
import NavBar from "./Components/NavBar/NavBar";
import Hero from "./Components/Hero/Hero";
import TopBar from "./Components/TopBar/TopBar";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Search from "./Pages/Search";


const App = () => {
  let heroData = [
    {text1:"Locating Events", text2: "Just Got Easier"}
  ]

  return (
    <BrowserRouter>
    
    <div>
      <Background />
      
      <NavBar />
      <Hero
        heroData = {heroData}
      />  
    </div>
    <Routes

    > <Route path="/search" element={
      <Search />
    }></Route></Routes>
    </BrowserRouter>
  )
}

export default App
