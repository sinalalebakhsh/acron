import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import cartService from "../features/cart/services/cartService";
import orderService from "../features/orders/services/orderService";

function Checkout() {
  const navigate = useNavigate();

  const [cart, setCart] = useState(null);
  const [addresses, setAddresses] = useState([]);

  const [selectedAddressId, setSelectedAddressId] = useState("");

  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;

    async function loadCheckoutData() {
      setLoading(true);
      setError("");

      try {
        const [cartData, addressData] = await Promise.all([
          cartService.getCart(),
          fetchAddresses(),
        ]);

        if (!isMounted) {
          return;
        }

        setCart(cartData);
        setAddresses(addressData);

        const defaultAddress = addressData.find(
          (address) => address.is_default
        );

        if (defaultAddress) {
          setSelectedAddressId(
            String(defaultAddress.id)
          );
        }
      } catch (err) {
        console.error(
          "Failed to load checkout data:",
          err
        );

        if (isMounted) {
          setError(
            "Unable to load checkout information."
          );
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    async function fetchAddresses() {
      const response = await fetch(
        "http://127.0.0.1:8000/api/customers/addresses/",
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem(
              "access_token"
            )}`,
          },
        }
      );

      if (!response.ok) {
        throw new Error(
          "Failed to load addresses."
        );
      }

      return response.json();
    }

    loadCheckoutData();

    return () => {
      isMounted = false;
    };
  }, []);

  async function handlePlaceOrder() {
    if (!selectedAddressId) {
      setError(
        "Please select a shipping address."
      );
      return;
    }

    if (!cart?.id) {
      setError(
        "Your cart could not be found."
      );
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      const order = await orderService.createOrder({
        cart_id: cart.id,
        address_id: Number(selectedAddressId),
      });

      navigate("/orders");
    } catch (err) {
      console.error(
        "Failed to create order:",
        err
      );

      setError(
        "Unable to place your order."
      );
    } finally {
      setSubmitting(false);
    }
  }

  if (loading) {
    return (
      <main className="page">
        <div className="page__container">
          <div className="page__header">
            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>Checkout</h1>

            <p>
              Loading checkout information...
            </p>
          </div>
        </div>
      </main>
    );
  }

  if (error && !cart) {
    return (
      <main className="page">
        <div className="page__container">
          <div className="page__header">
            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>Checkout</h1>

            <p>{error}</p>

            <Link to="/cart">
              Back to cart
            </Link>
          </div>
        </div>
      </main>
    );
  }

  if (!cart?.items?.length) {
    return (
      <main className="page">
        <div className="page__container">
          <div className="page__header">
            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>Your cart is empty</h1>

            <p>
              Add products to your cart before
              checking out.
            </p>

            <Link to="/products">
              Continue shopping
            </Link>
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

          <h1>Checkout</h1>

          <p>
            Review your order and select a
            shipping address.
          </p>
        </div>

        {error && (
          <div className="checkout-error">
            {error}
          </div>
        )}

        <section className="checkout">

          <div className="checkout__address">

            <h2>
              Shipping address
            </h2>

            {addresses.length === 0 ? (
              <div className="checkout__no-address">
                <p>
                  You do not have a shipping
                  address yet.
                </p>

                <Link to="/profile">
                  Add an address
                </Link>
              </div>
            ) : (
              <div className="checkout__addresses">

                {addresses.map((address) => (
                  <label
                    key={address.id}
                    className="checkout__address-card"
                  >
                    <input
                      type="radio"
                      name="shipping-address"
                      value={address.id}
                      checked={
                        selectedAddressId ===
                        String(address.id)
                      }
                      onChange={(event) =>
                        setSelectedAddressId(
                          event.target.value
                        )
                      }
                    />

                    <div>
                      <strong>
                        {address.title ||
                          "Address"}
                      </strong>

                      <p>
                        {address.receiver_name}
                      </p>

                      <p>
                        {address.province},{" "}
                        {address.city}
                      </p>

                      <p>
                        {address.street}
                      </p>

                      <p>
                        {address.postal_code}
                      </p>
                    </div>
                  </label>
                ))}

              </div>
            )}

          </div>

          <div className="checkout__summary">

            <h2>
              Order summary
            </h2>

            <div className="checkout__items">

              {cart.items.map((item) => (
                <div
                  key={item.id}
                  className="checkout__item"
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
                    {item.subtotal}
                  </span>
                </div>
              ))}

            </div>

            <div className="checkout__total">
              <span>
                Total
              </span>

              <strong>
                {cart.total_price}
              </strong>
            </div>

            <button
              type="button"
              className="checkout__button"
              disabled={
                submitting ||
                !selectedAddressId ||
                addresses.length === 0
              }
              onClick={handlePlaceOrder}
            >
              {submitting
                ? "Placing order..."
                : "Place order"}
            </button>

          </div>

        </section>

      </div>
    </main>
  );
}

export default Checkout;