function ProductSkeleton() {
  return (
    <article className="product-card product-card--skeleton">
      <div className="product-card__image skeleton-block" />

      <div className="product-card__content">

        <div className="skeleton-line skeleton-line--title" />

        <div className="skeleton-line" />

        <div className="skeleton-line skeleton-line--short" />

        <div className="product-card__footer">
          <div className="skeleton-line skeleton-line--price" />
          <div className="skeleton-button" />
        </div>

      </div>
    </article>
  );
}

export default ProductSkeleton;