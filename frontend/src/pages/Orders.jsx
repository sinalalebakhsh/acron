import { useEffect, useState } from "react";

import orderService from "../features/orders/services/orderService";

function Orders() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;

    async function loadOrders() {
      setLoading(true);
      setError("");

      try {
        const data = await orderService.getOrders();

        if (isMounted) {
          setOrders(data);
        }
      } catch (err) {
        console.error(
          "Failed to load orders:",
          err
        );

        if (isMounted) {
          setError(
            "Unable to load your orders."
          );
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    loadOrders();

    return () => {
      isMounted = false;
    };
  }, []);

  if (loading) {
    return (
      <main className="page">
        <div className="page__container">
          <div className="page__header">
            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>Your Orders</h1>

            <p>
              Loading your orders...
            </p>
          </div>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="page">
        <div className="page__container">
          <div className="page__header">
            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>Your Orders</h1>

            <p>{error}</p>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="page">
      <div className="page__container">

        <div className="page__header">
          <span className="page__eyebrow">
            ACRON STORE
          </span>

          <h1>Your Orders</h1>

          <p>
            Review your previous orders.
          </p>
        </div>

        {orders.length === 0 ? (
          <div className="orders-empty">
            <h2>No orders yet.</h2>

            <p>
              Your completed orders will
              appear here.
            </p>
          </div>
        ) : (
          <div className="orders-list">

            {orders.map((order) => (
              <article
                key={order.id}
                className="order-card"
              >

                <div className="order-card__header">

                  <div>
                    <span>
                      Order
                    </span>

                    <h2>
                      {order.id}
                    </h2>
                  </div>

                  <span>
                    {order.status}
                  </span>

                </div>

                <div className="order-card__date">
                  {new Date(
                    order.created_at
                  ).toLocaleString()}
                </div>

                <div className="order-card__items">

                  {order.items.map((item) => (
                    <div
                      key={item.id}
                      className="order-card__item"
                    >

                      <div>
                        <strong>
                          {item.product_name}
                        </strong>

                        <span>
                          Quantity: {item.quantity}
                        </span>
                      </div>

                      <span>
                        {item.unit_price}
                      </span>

                    </div>
                  ))}

                </div>

                <div className="order-card__total">

                  <span>
                    Total
                  </span>

                  <strong>
                    {order.total_price}
                  </strong>

                </div>

              </article>
            ))}

          </div>
        )}

      </div>
    </main>
  );
}

export default Orders;