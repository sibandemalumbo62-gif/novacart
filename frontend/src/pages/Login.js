import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./login.css";
import api from "../api/api";

function Login({ setLoggedIn }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const login = async () => {
    try {
      // Send form data (required by OAuth2PasswordRequestForm)
      const formData = new URLSearchParams();
      formData.append("username", username);
      formData.append("password", password);

      const res = await api.post("/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      // Save JWT
      localStorage.setItem("token", res.data.access_token);

      // Update login state
      setLoggedIn(true);

      // Redirect to dashboard
      navigate("/dashboard");

    } catch (err) {
      console.error("Login Error:", err);

      if (err.response) {
        console.log("Status:", err.response.status);
        console.log("Data:", err.response.data);

        alert(
          `Status: ${err.response.status}\n${JSON.stringify(err.response.data)}`
        );
      } else if (err.request) {
        alert("No response from backend. Is the backend running?");
      } else {
        alert(err.message);
      }
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h1>NovaCart</h1>
        <p>Product Management System</p>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={login}>Login</button>
      </div>
    </div>
  );
}

export default Login;