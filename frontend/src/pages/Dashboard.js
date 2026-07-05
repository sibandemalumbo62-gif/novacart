import { useEffect, useState } from "react";
import api from "../api/api";
import DashboardLayout from "./DashboardLayout";
import "./Dashboard.css";

function Dashboard({ setLoggedIn }) {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetch = async () => {
      const res = await api.get("/products");
      setProducts(res.data);
    };

    fetch();
  }, []);

  return (
    <DashboardLayout setLoggedIn={setLoggedIn}>
      <h1>Dashboard</h1>

      <div className="cards">
        <div className="card">
          <h3>Total Products</h3>
          <p>{products.length}</p>
        </div>

        <div className="card">
          <h3>Revenue</h3>
          <p>${products.length * 120}</p>
        </div>

        <div className="card">
          <h3>Active Users</h3>
          <p>{products.length * 7}</p>
        </div>
      </div>
    </DashboardLayout>
  );
}

export default Dashboard;