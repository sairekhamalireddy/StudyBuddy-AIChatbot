* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Arial, sans-serif;
  }

body {
background: linear-gradient(135deg, #667eea, #764ba2);
min-height: 100vh;
display: flex;
justify-content: center;
align-items: center;
padding: 15px;
}

.chat-container {
width: 100%;
max-width: 450px;
height: 600px;
background: white;
border-radius: 15px;
overflow: hidden;
box-shadow: 0 5px 20px rgba(0,0,0,0.3);
display: flex;
flex-direction: column;
}

header {
background: #5b5bd6;
color: white;
text-align: center;
padding: 20px;
}

header h1 {
margin-bottom: 5px;
}

#chat-box {
flex: 1;
padding: 15px;
overflow-y: auto;
display: flex;
flex-direction: column;
gap: 12px;
}

.bot-message,
.user-message {
padding: 12px;
border-radius: 10px;
max-width: 85%;
line-height: 1.5;
overflow-wrap: anywhere;
}

.bot-message {
background: #eeeeff;
color: #222;
align-self: flex-start;
}

.user-message {
background: #5b5bd6;
color: white;
align-self: flex-end;
}

.input-area {
display: flex;
padding: 12px;
gap: 8px;
border-top: 1px solid #ddd;
}

input {
flex: 1;
min-width: 0;
padding: 12px;
border: 1px solid #ccc;
border-radius: 8px;
outline: none;
}

button {
background: #5b5bd6;
color: white;
border: none;
padding: 12px 18px;
border-radius: 8px;
cursor: pointer;
}

button:hover {
background: #4141aa;
}

button:disabled {
opacity: 0.6;
cursor: not-allowed;
}
