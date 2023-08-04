const express = require('express');
const axios = require('axios');
require("dotenv").config()
const app = express();
const port = 3000;
const {createCompletionChatGTP} = require("./chatgptapi")

app.use(express(express.json()))

// API endpoint to generate Shayari
app.post('/shayari', async (req, res) => {
  const { program, language } = req.body;
  console.log(program,language)
  try {

    const msg= `Convert this  function add(a, b) {return a + b}  code to python programming language

     
  }`
  console.log(msg)
    const { data } = await createCompletionChatGTP({
        message:msg,
      }); 
    console.log(data)
    return res.json({ data});
  } catch (error) {
    return res.status(500).json({ error: 'Error generating Shayari.',err:error.message});
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
