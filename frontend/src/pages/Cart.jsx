import { Link } from "react-router-dom";

import { useCart } from "../context/CartContext";

function Cart() {
  const {
    cart,
    loading,
    updateQuantity,
    removeFromCart,
  } = useCart();

  if (loading) {
    return (
      <main className="page">
        <div className="page__container">
          <div className="page__header">
            <span className="page__eyebrow">
              ACRON STORE
            </span>

            <h1>Your Cart</h1>

            <p>
              Loading your cart...
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

            <h1>Your Cart</h1>

            <p>
              Your cart is currently empty.
            </p>
          </div>

          <Link
            to="/products"
            className="cart__continue-shopping"
          >
            Continue Shopping
          </Link>

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

          <h1>Your Cart</h1>

          <p>
            Review your selected products
            before continuing.
          </p>
        </div>

        <section className="cart">

          <div className="cart__items">

            {items.map((item) => (
              <article
                key={item.id}
                className="cart-item"
              >

                <div className="cart-item__image">

                  {item.product?.main_image ? (
                    <img
                      src={item.product.main_image}
                      alt={item.product.name}
                    />
                  ) : (
                    <div className="cart-item__no-image">
                      No image
                    </div>
                  )}

                </div>

                <div className="cart-item__content">

                  <Link
                    to={`/products/${item.product?.slug || ""}`}
                    className="cart-item__name"
                  >
                    {item.product?.name}
                  </Link>

                  <p className="cart-item__price">
                    {item.product?.price}
                  </p>

                  <div className="cart-item__actions">

                    <div className="cart-item__quantity">

                      <button
                        type="button"
                        onClick={() =>
                          updateQuantity(
                            item.id,
                            item.quantity - 1
                          )
                        }
                        disabled={
                          item.quantity <= 1
                        }
                        aria-label="Decrease quantity"
                      >
                        −
                      </button>

                      <span>
                        {item.quantity}
                      </span>

                      <button
                        type="button"
                        onClick={() =>
                          updateQuantity(
                            item.id,
                            item.quantity + 1
                          )
                        }
                        aria-label="Increase quantity"
                      >
                        +
                      </button>

                    </div>

                    <button
                      type="button"
                      className="cart-item__remove"
                      onClick={() =>
                        removeFromCart(item.id)
                      }
                    >
                      Remove
                    </button>

                  </div>

                </div>

                <div className="cart-item__total">
                  {item.total_price}
                </div>

              </article>
            ))}

          </div>

          <aside className="cart__summary">

            <h2>
              Cart Summary
            </h2>

            <div className="cart__summary-row">

              <span>
                Subtotal
              </span>

              <strong>
                {cart.total_price}
              </strong>

            </div>

            <div className="cart__summary-divider" />

            <div className="cart__summary-row cart__summary-row--total">

              <span>
                Total
              </span>

              <strong>
                {cart.total_price}
              </strong>

            </div>

            <button
              type="button"
              className="cart__checkout-button"
            >
              Proceed to Checkout
            </button>

            <Link
              to="/products"
              className="cart__continue-shopping"
            >
              Continue Shopping
            </Link>

          </aside>

        </section>

      </div>

    </main>
  );
}

export default Cart;