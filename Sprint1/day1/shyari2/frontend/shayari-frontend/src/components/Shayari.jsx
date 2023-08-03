import React, { useState } from 'react';
import axios from 'axios';

const Shayari = () => {
  const [keyword, setKeyword] = useState('');
  const [shayari, setShayari] = useState([]);

  const generateShayari = async () => {
    try {
      const response = await axios.get(`https://apishyari.onrender.com/shayari?keyword=${encodeURIComponent(keyword)}`);
      const formattedShayari = response.data.contentArray.split('\n').map(sentence => sentence.trim());
      setShayari(formattedShayari);
    } catch (error) {
      console.error('Error generating Shayari:', error.message);
      setShayari(['Error generating Shayari.']);
    }
  };

  return (
    <div className="shayari-container p-4 max-w-md mx-auto card">
      <h1 className="text-2xl font-bold mb-4">Shayari App</h1>
      <div className="mb-4">
        <input
          type="text"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          placeholder="Enter a keyword"
          className="w-full px-4 py-2 rounded-md border border-gray-300 focus:ring-2 focus:ring-indigo-300 input"
        />
      </div>
      <button
        onClick={generateShayari}
        className="px-4 py-2 bg-indigo-500 text-white rounded-md"
      >
        Generate Shayari
      </button>
      <div className="mt-4">
        {shayari && shayari.map((sentence, index) => (
          <p
            key={index}
            className="border border-gray-300 p-4 rounded-md bg-gray-100 mb-2"
          >
            {sentence}
          </p>
        ))}
      </div>
    </div>
  );
};

export default Shayari;
