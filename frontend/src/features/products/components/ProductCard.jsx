import { useState } from "react";
import { Link } from "react-router-dom";

import { useCart } from "../../../context/CartContext";

function ProductCard({ product }) {
  const isAvailable =
    product.inventory > 0;

  const { addToCart } = useCart();

  const [addingToCart, setAddingToCart] =
    useState(false);

  const handleAddToCart = async () => {
    if (!isAvailable) {
      return;
    }

    setAddingToCart(true);

    try {
      await addToCart(product.id);
    } catch (error) {
      console.error(
        "Failed to add product to cart:",
        error
      );
    } finally {
      setAddingToCart(false);
    }
  };

  return (
    <article className="product-card">

      <Link
        to={`/products/${product.slug}`}
        className="product-card__image-link"
      >
        <div className="product-card__image">

          {product.main_image ? (
            <img
              src={product.main_image}
              alt={product.name}
              loading="lazy"
            />
          ) : (
            <div className="product-card__no-image">
              No image
            </div>
          )}

        </div>
      </Link>

      <div className="product-card__content">

        {product.brand?.name && (
          <span className="product-card__brand">
            {product.brand.name}
          </span>
        )}

        <Link
          to={`/products/${product.slug}`}
          className="product-card__title"
        >
          {product.name}
        </Link>

        <p className="product-card__description">
          {product.description}
        </p>

        <div className="product-card__footer">

          <div>
            <span className="product-card__price">
              {product.price}
            </span>
          </div>

          <span
            className={
              isAvailable
                ? "product-card__stock product-card__stock--available"
                : "product-card__stock product-card__stock--unavailable"
            }
          >
            {isAvailable
              ? "In stock"
              : "Out of stock"}
          </span>

        </div>

        <button
          type="button"
          className="product-card__cart-button"
          disabled={
            !isAvailable ||
            addingToCart
          }
          onClick={handleAddToCart}
        >
          {addingToCart
            ? "Adding..."
            : "Add to cart"}
        </button>

      </div>

    </article>
  );
}

export default ProductCard;