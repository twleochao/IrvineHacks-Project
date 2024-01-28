import './NavBar.css'
import { Link } from "react-router-dom";



const NavBar = () => {
  return (
    <div className='Bar'>
      <div className='nav'>
        <div className='navLogo'>ZOT EVENTS</div>
        <ul className="nav-menu">
          <li>
            <Link to="/search">START LOOKING</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default NavBar
