#!/usr/bin/env python3
"""
GUI Client for CSE 310 Networking Module
Uses Tkinter for UI and TCP sockets for communication.
"""

import socket
import json
import tkinter as tk
from tkinter import messagebox

HOST = "127.0.0.1"
PORT = 5050


class StoryClientGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Interactive Network Story")

        # Socket setup
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        # UI Elements
        self.text_area = tk.Text(root, height=15, width=70, wrap="word")
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state="disabled")

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.buttons = {}
        for key in ["A", "B", "C"]:
            btn = tk.Button(
                self.button_frame,
                text=key,              # placeholder, will be updated per scene
                width=25,
                command=lambda k=key: self.send_choice(k),
                wraplength=180,
                justify="center"
            )
            btn.pack(side="left", padx=5)
            self.buttons[key] = btn


        self.restart_btn = tk.Button(root, text="Restart", command=self.restart)
        self.restart_btn.pack(pady=5)

        # Start game
        self.receive_scene()

    def send_json(self, data: dict) -> None:
        """Send JSON message to server."""
        self.sock.sendall((json.dumps(data) + "\n").encode("utf-8"))

    def recv_json(self) -> dict:
        """Receive JSON message from server."""
        buffer = b""
        while b"\n" not in buffer:
            buffer += self.sock.recv(4096)
        return json.loads(buffer.decode("utf-8"))

    def receive_scene(self) -> None:
        """Receive and display scene from server."""
        msg = self.recv_json()
        self.display_scene(msg)

    def display_scene(self, msg: dict) -> None:
        """Update UI with scene text and choices."""
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)

        scene = msg.get("scene", {})
        self.text_area.insert(tk.END, scene.get("text", ""))

        self.text_area.config(state="disabled")

        choices = scene.get("choices", [])

        # Disable all buttons first
        for btn in self.buttons.values():
            btn.config(state="disabled", text="")

        # Enable and label buttons based on choices
        for choice in choices:
            key = choice["key"].upper()
            label = f"{key}: {choice['label']}"
            if key in self.buttons:
                self.buttons[key].config(
                    state="normal",
                    text=label
                )

        # If end scene, show message
        if msg.get("end"):
            messagebox.showinfo(
                "End of Story",
                "You reached an ending.\nClick Restart to play again."
            )
        else:
            for btn in self.buttons.values():
                btn.config(state="normal")

    def send_choice(self, choice: str) -> None:
        """Send player choice to server."""
        self.send_json({"action": "choose", "choice": choice})
        msg = self.recv_json()
        self.display_scene(msg)

    def restart(self) -> None:
        """Restart the story."""
        self.send_json({"action": "restart"})
        msg = self.recv_json()
        self.display_scene(msg)


def main():
    root = tk.Tk()
    app = StoryClientGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()