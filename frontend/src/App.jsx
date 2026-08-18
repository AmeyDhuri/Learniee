import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./Login"
import Signup from "./Signup"
import Dashboard from "./Dashboard"
import ProtectedRoute from "./ProtectedRoute"
import "./App.css"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>}/>

        <Route path="/" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App