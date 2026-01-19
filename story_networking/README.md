---

## Module Information

**Course:** CSE 310 – Applied Programming  
**Module:** Module 1 – Networking  
**Student Name:** Christiaan Wolmarans  

---

## Module Requirements Checklist

### Networking Requirements
- **Client sends requests to server and receives responses:** Yes  
- **Protocol used:** TCP  
- **Responses are displayed and used by the client:** Yes  

### Additional Requirement (One Required)
- **Graphical User Interface (GUI) provided instead of command line:** Yes  
  - The client application uses a Tkinter GUI to display story text and interactive choices.

---

## Request Types Supported

The server supports multiple request types sent by the client:
1. **choose** – Sent when the user selects a story option (A, B, or C)
2. **restart** – Resets the story to the starting scene
3. **quit** – Ends the client session and closes the connection

All requests and responses are sent as JSON messages over a TCP connection.

---

## Time Log Summary

Approximate total time spent on this module: **22.5 hours**

- Planning & requirements review: 3.5 hours  
- Server networking implementation: 4.0 hours  
- Story design & logic: 3.5 hours  
- Client implementation & GUI development: 4.5 hours  
- Integration, debugging & polish: 3.5 hours  
- Documentation & video recording: 4.0 hours  

---

## Learning Reflection

This module reinforced the importance of breaking large problems into smaller, manageable steps. Starting with basic networking functionality before adding story logic and a GUI made the project easier to understand and debug. Testing frequently helped catch errors early and improved my understanding of how client–server communication works in practice.

One challenge was underestimating the time required to implement a graphical interface. In future modules, I plan to spend more time planning unfamiliar components before coding and set clearer milestones to track progress. This will help improve time management and reduce rework in later stages of development.

---
