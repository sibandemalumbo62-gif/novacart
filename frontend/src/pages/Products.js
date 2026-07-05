import { useEffect, useState } from "react";
import api from "../api/api";
import DashboardLayout from "./DashboardLayout";
import "./Products.css";

function Products({ setLoggedIn }) {
  const [products, setProducts] = useState([]);
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");

  // Fetch products
  const fetchProducts = async () => {
    try {
      const res = await api.get("/products");
      setProducts(res.data);
    } catch (err) {
      console.error("Failed to fetch products:", err);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  // Add product
  const addProduct = async () => {
    if (!name || !price) return;

    try {
      await api.post("/products", {
        name,
        price,
      });

      setName("");
      setPrice("");
      fetchProducts();
    } catch (err) {
      console.error("Failed to add product:", err);
    }
  };

  // Delete product
  const deleteProduct = async (id) => {
    try {
      await api.delete(`/products/${id}`);
      fetchProducts();
    } catch (err) {
      console.error("Failed to delete product:", err);
    }
  };

  return (
    <DashboardLayout setLoggedIn={setLoggedIn}>
      <h1>Products</h1>

      {/* Add Product Form */}
      <div className="form">
        <input
          placeholder="Product name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          placeholder="Price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />

        <button onClick={addProduct}>Add Product</button>
      </div>

      {/* Product Grid */}
      <div className="product-grid">
        {products.length === 0 ? (
          <p>No products found</p>
        ) : (
          products.map((p) => (
            <div key={p.id} className="product-card">
              <h3>{p.name}</h3>
              <p>${p.price}</p>

              <button
                className="delete-btn"
                onClick={() => deleteProduct(p.id)}
              >
                Delete
              </button>
            </div>
          ))
        )}
      </div>
    </DashboardLayout>
  );
}

export default Products;