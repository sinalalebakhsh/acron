import { Link, NavLink } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

function Navbar() {
  const {
    user,
    isAuthenticated,
    logout,
  } = useAuth();

  const navLinkClass = ({ isActive }) =>
    `navbar__link ${isActive ? "navbar__link--active" : ""}`;

  return (
    <header className="navbar">
      <div className="navbar__container">

        <Link to="/" className="navbar__brand">
          ACRON
        </Link>

        <nav className="navbar__navigation">
          <NavLink to="/" className={navLinkClass}>
            Home
          </NavLink>

          <NavLink
            to="/products"
            className={navLinkClass}
          >
            Products
          </NavLink>

          <NavLink
            to="/cart"
            className={navLinkClass}
          >
            Cart
          </NavLink>

          {isAuthenticated && (
            <NavLink
              to="/orders"
              className={navLinkClass}
            >
              Orders
            </NavLink>
          )}
        </nav>

        <div className="navbar__account">

          {isAuthenticated ? (
            <>
              <span className="navbar__user">
                {user?.username}
              </span>

              <button
                className="navbar__logout"
                onClick={logout}
              >
                Logout
              </button>
            </>
          ) : (
            <Link
              to="/login"
              className="navbar__login"
            >
              Login
            </Link>
          )}

        </div>

      </div>
    </header>
  );
}

export default Navbar;