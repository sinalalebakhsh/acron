import { useEffect, useState } from "react";

import ProductGrid from "../features/products/components/ProductGrid";
import { getProducts } from "../features/products/services/productService";

function Products() {
  const [products, setProducts] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [page, setPage] = useState(1);

  const [pagination, setPagination] = useState({
    count: 0,
    next: null,
    previous: null,
  });

  useEffect(() => {
    let isMounted = true;

    async function loadProducts() {
      setLoading(true);
      setError("");

      try {
        const data = await getProducts(page);

        if (!isMounted) {
          return;
        }

        /*
         * Django REST Framework pagination normally
         * returns:
         *
         * {
         *   count,
         *   next,
         *   previous,
         *   results
         * }
         *
         * If pagination is ever disabled and the API
         * returns an array, we support that too.
         */

        if (Array.isArray(data)) {
          setProducts(data);

          setPagination({
            count: data.length,
            next: null,
            previous: null,
          });
        } else {
          setProducts(data.results ?? []);

          setPagination({
            count: data.count ?? 0,
            next: data.next ?? null,
            previous: data.previous ?? null,
          });
        }
      } catch (err) {
        if (!isMounted) {
          return;
        }

        console.error(
          "Failed to load products:",
          err
        );

        setError(
          "Unable to load products. Please try again."
        );
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    loadProducts();

    return () => {
      isMounted = false;
    };
  }, [page]);

  const hasNextPage = Boolean(pagination.next);
  const hasPreviousPage = Boolean(
    pagination.previous
  );

  return (
    <main className="page">

      <div className="page__container">

        <header className="page__header">

          <span className="page__eyebrow">
            ACRON STORE
          </span>

          <h1>Products</h1>

          <p>
            Explore the ACRON product catalog.
          </p>

        </header>

        {error ? (
          <div className="products-error">

            <h2>
              Something went wrong
            </h2>

            <p>
              {error}
            </p>

            <button
              type="button"
              onClick={() => setPage(1)}
            >
              Try again
            </button>

          </div>
        ) : (
          <>
            <ProductGrid
              products={products}
              loading={loading}
            />

            {!loading &&
              (hasPreviousPage ||
                hasNextPage) && (
                <div className="pagination">

                  <button
                    type="button"
                    disabled={!hasPreviousPage}
                    onClick={() =>
                      setPage((current) =>
                        Math.max(
                          1,
                          current - 1
                        )
                      )
                    }
                  >
                    Previous
                  </button>

                  <span>
                    Page {page}
                  </span>

                  <button
                    type="button"
                    disabled={!hasNextPage}
                    onClick={() =>
                      setPage(
                        (current) =>
                          current + 1
                      )
                    }
                  >
                    Next
                  </button>

                </div>
              )}
          </>
        )}

      </div>

    </main>
  );
}

export default Products;