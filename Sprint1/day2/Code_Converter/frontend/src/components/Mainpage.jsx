import React, { useState } from 'react';
import MonacoEditor from '@monaco-editor/react';
import axios from "axios"
import './NavBar.css';
const MainPage = () => {
  const [code, setCode] = useState('// Write your code here...');
  const [selectedLanguage, setSelectedLanguage] = useState('javascript');
 const [converterlanguage,setconverterlanguage ] =  useState("")
 const [convertedCode, setConvertedCode] = useState('');
  const handleCodeChange = (value) => {
    setCode(value);
  };
  const languages = [
    { value: 'javascript', label: 'JavaScript' },
    { value: 'python', label: 'Python' },
    { value: 'java', label: 'Java' },
    { value: 'cpp', label: 'C++' },
    { value: 'ruby', label: 'Ruby' },
    // Add more languages here
    { value: 'csharp', label: 'C#' },
    { value: 'php', label: 'PHP' },
    { value: 'swift', label: 'Swift' },
    { value: 'typescript', label: 'TypeScript' },
  ];
  const handleLanguageChange = (event) => {
    setSelectedLanguage(event.target.value);
  };
  const handleCodeConverter=async(e)=>{
    e.preventDefault();
    const newpayload={
        code:code,
        language:converterlanguage
    }

    try {
        const response = await axios.post('https://codeconverterdebugger.onrender.com/api/convert-code', newpayload);
        console.log(response.data.convertedCode)
        setConvertedCode(response.data.convertedCode);
      } catch (error) {
        console.error(error);
      }
  
  }
  const handledebug=async(e)=>{
    e.preventDefault();
    try {
        const response = await axios.post('https://codeconverterdebugger.onrender.com/api/debug', {code});
        console.log(response.data.convertedCode)
        setConvertedCode(response.data.convertedCode);
      } catch (error) {
        console.error(error);
      }
  }
  const handlequalitycheck=async(e)=>{
    e.preventDefault();
    try {
        const response = await axios.post('https://codeconverterdebugger.onrender.com/api/quality', {code});
        console.log(response.data.convertedCode)
        setConvertedCode(response.data.convertedCode);
      } catch (error) {
        console.error(error);
      }
  }
  return (
    <div>
     <nav className="navbar">
      <div className="navbar-buttons">
        {/* Select Tag */}
        <select className="language-select" value={converterlanguage}onChange={((e)=>setconverterlanguage(e.target.value))}>
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
        <button className="debug-btn" onClick={((e)=>handleCodeConverter(e))}>Convert</button>
      </div>

      {/* Convert Button */}
      <button className="convert-btn"onClick={((e)=>handledebug(e))} >Debug</button>
      <button className="convert-btn"onClick={((e)=>handlequalitycheck(e))} >Quality</button>
    </nav>
      <div >
          <select
            className="bg-white text-gray-900 font-bold py-2 px-4 rounded"
            value={selectedLanguage}
            onChange={handleLanguageChange}
          >
            {languages.map((lang) => (
              <option key={lang.value} value={lang.value}>
                {lang.label}
              </option>
            ))}
          </select>
        </div>
      <div className="flex">
        {/* Left Section with Monaco Editor */}
        

        {/* Left Section with Monaco Editor */}
        <div className="w-5/6 h-screen p-4">
          <MonacoEditor
            // Full width of the left section
            height="100%" // Full screen height
            language={selectedLanguage}
            theme="vs-dark"
            value={code}
            onChange={handleCodeChange}
          />
        </div>

        {/* Right Section */}
        <div className="white w-1/2 h-screen p-4 bg-gray-100 ">
          {/* Display the code somewhere else */}
          <pre> <b>Output:</b> {"\n"}  {"\n"}  {"\n"}    {convertedCode}</pre>
        </div>
      </div>
    </div>
  );
};

export default MainPage;
