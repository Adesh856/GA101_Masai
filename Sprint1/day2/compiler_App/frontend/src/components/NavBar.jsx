import React from 'react';
import './NavBar.css'; // Import the CSS file for NavBar styling

const NavBar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-buttons">
        {/* Select Tag */}
        <select className="language-select">
          <option value="">Select Language</option>
          <option value="javascript">JavaScript</option>
          <option value="python">Python</option>
          {/* Add more language options here */}
          {/* For example: */}
          <option value="java">Java</option>
          <option value="cpp">C++</option>
          <option value="ruby">Ruby</option>
          {/* ...and so on */}
        </select>

        {/* Debug Button */}
        <button className="debug-btn">Convert</button>
      </div>

      {/* Convert Button */}
      <button className="convert-btn">Debug</button>
    </nav>
  );
};

export default NavBar;
