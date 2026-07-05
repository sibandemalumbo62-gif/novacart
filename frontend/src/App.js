import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useState } from "react";

import Login from "./pages/Login";
import Products from "./pages/Products";
import Dashboard from "./pages/Dashboard";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  const [loggedIn, setLoggedIn] = useState(
    !!localStorage.getItem("token")
  );

  return (
    <BrowserRouter>
      <Routes>

        {/* Default redirect */}
        <Route
          path="/"
          element={
            loggedIn ? (
              <Navigate to="/dashboard" />
            ) : (
              <Navigate to="/login" />
            )
          }
        />

        {/* Login */}
        <Route
          path="/login"
          element={<Login setLoggedIn={setLoggedIn} />}
        />

        {/* Dashboard (NEW) */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard setLoggedIn={setLoggedIn} />
            </ProtectedRoute>
          }
        />

        {/* Products */}
        <Route
          path="/products"
          element={
            <ProtectedRoute>
              <Products setLoggedIn={setLoggedIn} />
            </ProtectedRoute>
          }
        />

        {/* Fallback */}
        <Route
          path="*"
          element={<Navigate to="/" />}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;