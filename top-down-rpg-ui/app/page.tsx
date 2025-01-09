"use client";

import PixiComponent from "@/_components/pixiComponent";
import { useEffect } from "react";

const websocketHost = "192.168.0.16";
const websocketPort = 8000;
const isSecure = false;

const websocketAddress = `${isSecure ? "wss" : "ws"}://${websocketHost}:${websocketPort}`;

export default function Home() {

  useEffect(() => {
    const socket = new WebSocket(websocketAddress);
  
    socket.onopen = () => {
      console.log("Connected to the websocket server");
      socket.send(JSON.stringify("hello"));
    };
  
    socket.onmessage = (event) => {
      console.log("Message from server: ", event.data);
    };
  
    socket.onerror = (error) => {
      console.error("WebSocket error: ", error);
    };
  
    socket.onclose = () => {
      console.log("WebSocket connection closed");
    };
  
    return () => {
      socket.close();
    };
  }, []);

  return (
    <main className="">
      <PixiComponent />
    </main>
  );
}
