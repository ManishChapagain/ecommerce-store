import { useEffect, useState } from "react";
import { addToCart, checkout, fetchCart, fetchItems, fetchReport } from "./api";
import { CartItem, DiscountCode, Report } from "./types";

// hardcoded user id for now
const userId = "1";

function App() {
  const [items, setItems] = useState([]);
  const [cart, setCart] = useState<CartItem[]>([]);
  const [discountCode, setDiscountCode] = useState("");
  const [message, setMessage] = useState("");
  const [report, setReport] = useState<Report | null>(null);

  useEffect(() => {
    const initializeData = async () => {
      const [itemsData, cartData, reportData] = await Promise.all([
        fetchItems(),
        fetchCart(userId),
        fetchReport(),
      ]);

      setItems(itemsData.items);
      setCart(cartData);
      setReport(reportData);
    };

    initializeData();
  }, []);

  const handleAddToCart = async (item: CartItem) => {
    const data = await addToCart(userId, { ...item, qty: 1 });
    setCart(data.cart);
  };

  const handleCheckout = async () => {
    const data = await checkout(userId, discountCode.trim());
    if (data.error) {
      setMessage(data.error);
    } else {
      setMessage(`${data.message}. Total: $${data.total}`);
      setCart([]);
      setReport(await fetchReport());
    }

    setDiscountCode("");
    // clear the cart message after 3 seconds
    setTimeout(() => {
      setMessage("");
    }, 5000);
  };

  return (
    <div style={{ display: "flex", padding: 20, gap: 40 }}>
      <div
        style={{
          border: "1px solid",
          padding: "1rem",
          marginTop: "2rem",
        }}
      >
        <h2>Items</h2>
        {items.map((item: any) => (
          <div key={item.id} style={{ marginBottom: 10 }}>
            <strong>{item.name}</strong> - ${item.price}
            <button
              onClick={() => handleAddToCart(item)}
              style={{ marginLeft: 10 }}
            >
              Add to Cart
            </button>
          </div>
        ))}
      </div>

      <div
        style={{
          border: "1px solid",
          padding: "1rem",
          marginTop: "2rem",
        }}
      >
        <h2>Cart</h2>
        {cart.length === 0 ? (
          <p>No items in cart.</p>
        ) : (
          <ul>
            {cart.map((item: CartItem) => (
              <li key={item.id}>
                {item.name} x {item.qty}
              </li>
            ))}
          </ul>
        )}

        <input
          type="text"
          placeholder="Discount Code"
          value={discountCode}
          onChange={(e) => setDiscountCode(e.target.value)}
          style={{ marginTop: 10 }}
        />
        <br />
        <button onClick={handleCheckout} style={{ marginTop: 10 }}>
          Checkout
        </button>
        {message && <p>{message}</p>}
      </div>

      <div
        style={{
          border: "1px solid",
          padding: "1rem",
          marginTop: "2rem",
        }}
      >
        <h2>Admin Panel</h2>
        <p>
          <strong>Total Items Sold:</strong> {report?.total_items_sold || "0"}
        </p>
        <p>
          <strong>Total Revenue:</strong> ${report?.total_revenue}
        </p>
        <p>
          <strong>Total Discount Given:</strong> ${report?.total_discount_given}
        </p>

        <strong>Discount Codes:</strong>
        {report?.discount_codes.length ? (
          <ul>
            {report?.discount_codes.map((codeObj: DiscountCode, i) => (
              <li key={i}>
                {codeObj.code} — {codeObj.used ? "Used" : "Unused"}
              </li>
            ))}
          </ul>
        ) : (
          <p>No discount codes available.</p>
        )}
      </div>
    </div>
  );
}

export default App;
