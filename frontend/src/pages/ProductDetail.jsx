import { Link, useParams } from "react-router-dom";
import { useEffect, useState } from "react";

import { getProductBySlug } from "../features/products/services/productService";

function ProductDetail() {
  const { slug } = useParams();

  const [product, setProduct] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {
    let isMounted = true;

    async function loadProduct() {
      setLoading(true);
      setError("");

      try {
        const data =
          await getProductBySlug(slug);

        if (isMounted) {
          setProduct(data);
        }
      } catch (err) {
        console.error(
          "Failed to load product:",
          err
        );

        if (isMounted) {
          setError(
            "Unable to load this product."
          );
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    if (slug) {
      loadProduct();
    }

    return () => {
      isMounted = false;
    };
  }, [slug]);

  if (loading) {
    return (
      <main className="page">
        <div className="page__container">
          <div className="product-detail-loading">
            Loading product...
          </div>
        </div>
      </main>
    );
  }

  if (error || !product) {
    return (
      <main className="page">
        <div className="page__container">

          <div className="product-detail-error">

            <h1>
              Product not found
            </h1>

            <p>
              {error ||
                "This product does not exist."}
            </p>

            <Link to="/products">
              Back to products
            </Link>

          </div>

        </div>
      </main>
    );
  }

  const isAvailable =
    product.inventory > 0;

  return (
    <main className="page">

      <div className="page__container">

        <Link
          to="/products"
          className="product-detail__back"
        >
          ← Back to products
        </Link>

        <section className="product-detail">

          <div className="product-detail__media">

            {product.main_image ? (
              <img
                src={product.main_image}
                alt={product.name}
              />
            ) : (
              <div className="product-detail__no-image">
                No image
              </div>
            )}

          </div>

          <div className="product-detail__content">

            {product.brand?.name && (
              <span className="product-detail__brand">
                {product.brand.name}
              </span>
            )}

            <h1>
              {product.name}
            </h1>

            {product.category?.name && (
              <span className="product-detail__category">
                {product.category.name}
              </span>
            )}

            <p className="product-detail__description">
              {product.description}
            </p>

            <div className="product-detail__price">
              {product.price}
            </div>

            <div
              className={
                isAvailable
                  ? "product-detail__stock product-detail__stock--available"
                  : "product-detail__stock product-detail__stock--unavailable"
              }
            >
              {isAvailable
                ? `${product.inventory} available`
                : "Out of stock"}
            </div>

            <button
              type="button"
              className="product-detail__cart-button"
              disabled={!isAvailable}
            >
              Add to cart
            </button>

          </div>

        </section>

      </div>

    </main>
  );
}

export default ProductDetail;