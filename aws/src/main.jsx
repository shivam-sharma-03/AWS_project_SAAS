// main.jsx
import React from "react";
import ReactDOM from "react-dom/client";
import SarcasmRoaster from "./App.jsx";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <SarcasmRoaster />
  </React.StrictMode>
);