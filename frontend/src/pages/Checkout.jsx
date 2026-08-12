import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { useCart } from "../context/CartContext";
import customerService from "../features/customers/services/customerService";
import orderService from "../features/orders/services/orderService";

function Checkout() {
  const navigate = useNavigate();

  const {
    cart,
    loading: cartLoading,
  } = useCart();

  const [addresses, setAddresses] = useState([]);
  const [selectedAddressId, setSelectedAddressId] =
    useState("");

  const [loadingAddresses, setLoadingAddresses] =
    useState(true);

  const [submitting, setSubmitting] =
    useState(false);

  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;

    async function loadAddresses() {
      setLoadingAddresses(true);
      setError("");

      try {
        const data =
          await customerService.getAddresses();

        if (!isMounted) {
          return;
        }

        setAddresses(data);

        const defaultAddress = data.find(
          (address) => address.is_default
        );

        if (defaultAddress) {
          setSelectedAddressId(
            String(defaultAddress.id)
          );
        } else if (data.length > 0) {
          setSelectedAddressId(
            String(data[0].id)
          );
        }
      } catch (err) {
        console.error(
          "Failed to load addresses:",
          err
        );

        if (isMounted) {
          setError(
            "Unable to load your addresses."
          );
        }
      } finally {
        if (isMounted) {
          setLoadingAddresses(false);
        }
      }
    }

    loadAddresses();

    return () => {
      isMounted = false;
    };
  }, []);

  const handlePlaceOrder = async () => {
    if (!selectedAddressId) {
      setError(
        "Please select a shipping address."
      );
      return;
    }

    if (!cart?.id) {
      setError(
        "Your cart could not be identified."
      );
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      const order =
        await orderService.createOrder(
          cart.id,
          Number(selectedAddressId)
        );

      console.log(
        "Order created successfully:",
        order
      );

      navigate("/orders");
    } catch (err) {
      console.error(
        "Failed to create order:",
        err
      );

      setError(
        err.response?.data?.detail ||
          "Unable to place your order."
      );
    } finally {
      setSubmitting(false);
    }
  };

  if (cartLoading || loadingAddresses) {
    return (
      <main className="page">
        <div className="page__container">

          <div className="page__header">

            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>
              Checkout
            </h1>

            <p>
              Loading checkout information...
            </p>

          </div>

        </div>
      </main>
    );
  }

  const items = cart?.items || [];

  if (items.length === 0) {
    return (
      <main className="page">
        <div className="page__container">

          <div className="page__header">

            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>
              Your cart is empty
            </h1>

            <p>
              Add products to your cart
              before checking out.
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

          <h1>
            Checkout
          </h1>

          <p>
            Review your order and select
            a shipping address.
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

                <p>
                  Please add an address before
                  placing your order.
                </p>

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

                      <p>
                        {address.phone_number}
                      </p>

                      {address.is_default && (
                        <span>
                          Default address
                        </span>
                      )}

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

              {items.map((item) => (
                <div
                  key={item.id}
                  className="checkout__item"
                >

                  <div>

                    <strong>
                      {item.product?.name ||
                        item.product_name}
                    </strong>

                    <span>
                      Quantity: {item.quantity}
                    </span>

                  </div>

                  <span>
                    {item.total_price ||
                      item.subtotal}
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

            <Link to="/cart">
              Back to cart
            </Link>

          </div>

        </section>

      </div>

    </main>
  );
}

export default Checkout;
