#!/usr/bin/env python3
# server.py
# TCP Server that manages the story state.
# Client sends JSON messages. Server responds JSON.

import socket
import threading
import json
from typing import Dict, Any, Tuple
from story import get_scene, validate_choice, is_end_scene

HOST = "127.0.0.1"
PORT = 5050

def send_json(conn: socket.socket, obj: Dict[str, Any]) -> None:
    """Send a JSON object followed by newline (NDJSON)."""
    data = (json.dumps(obj) + "\n").encode("utf-8")
    conn.sendall(data)

def recv_line(conn: socket.socket) -> str:
    """Receive a line terminated by newline."""
    buffer = b""
    while b"\n" not in buffer:
        chunk = conn.recv(4096)
        if not chunk:
            break
        buffer += chunk
    return buffer.decode("utf-8").strip()

def handle_client(conn: socket.socket, addr: Tuple[str, int]) -> None:
    """
    Handles one client connection.
    Protocol messages:
      - {"action":"start"} -> returns starting scene
      - {"action":"choose","scene":"start","choice":"A"} -> returns next scene
    """
    print(f"[+] Client connected: {addr}")

    # Each client starts at "start"
    current_scene = "start"

    try:
        # Immediately send the starting scene so the client can display it
        scene = get_scene(current_scene)
        send_json(conn, {"ok": True, "scene_id": current_scene, "scene": scene, "end": is_end_scene(current_scene)})

        while True:
            line = recv_line(conn)
            if not line:
                break

            try:
                req = json.loads(line)
            except json.JSONDecodeError:
                send_json(conn, {"ok": False, "error": "Invalid JSON request."})
                continue

            action = req.get("action")

            if action == "choose":
                choice = str(req.get("choice", "")).strip().upper()
                # Validate and move
                next_scene = validate_choice(current_scene, choice)

                if next_scene == current_scene:
                    # invalid choice
                    scene = get_scene(current_scene)
                    send_json(conn, {"ok": False, "error": "Invalid choice. Try again.", "scene_id": current_scene, "scene": scene, "end": is_end_scene(current_scene)})
                    continue

                current_scene = next_scene
                scene = get_scene(current_scene)
                send_json(conn, {"ok": True, "scene_id": current_scene, "scene": scene, "end": is_end_scene(current_scene)})

            elif action == "restart":
                current_scene = "start"
                scene = get_scene(current_scene)
                send_json(conn, {"ok": True, "scene_id": current_scene, "scene": scene, "end": is_end_scene(current_scene)})

            elif action == "quit":
                send_json(conn, {"ok": True, "message": "Goodbye!"})
                break

            else:
                send_json(conn, {"ok": False, "error": "Unknown action."})

    except ConnectionResetError:
        print(f"[!] Client disconnected unexpectedly: {addr}")
    finally:
        conn.close()
        print(f"[-] Connection closed: {addr}")

def main() -> None:
    """Start the TCP server."""
    print(f"Starting server on {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print("Server listening...")

        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()
