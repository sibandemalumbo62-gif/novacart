import { NavLink, useNavigate } from "react-router-dom";
import "./DashboardLayout.css";
import { FiBox, FiHome, FiLogOut } from "react-icons/fi";

function DashboardLayout({ children, setLoggedIn }) {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    setLoggedIn(false);
    navigate("/login");
  };

  return (
    <div className="dashboard">
      <div className="sidebar">
        <h2>NovaCart</h2>

        <nav>
          <NavLink
  to="/dashboard"
  className={({ isActive }) =>
    isActive ? "nav-item active" : "nav-item"
  }
>
  <FiHome style={{ marginRight: "8px" }} />
  Dashboard
</NavLink>

<NavLink
  to="/products"
  className={({ isActive }) =>
    isActive ? "nav-item active" : "nav-item"
  }
>
  <FiBox style={{ marginRight: "8px" }} />
  Products
</NavLink>
        </nav>

        <button onClick={logout} className="logout-btn">
          <FiLogOut style={{ marginRight: "8px" }} />
          Logout
        </button>
      </div>

      <div className="main">
        {children}
      </div>
    </div>
  );
}

export default DashboardLayout;