# sticky-notes-application
A simple Django-based Sticky Note web application that lets users create, view, update, and delete colorful digital notes. Designed for quick idea capture and easy organization, built with clean UI and test-driven development.

---
## How It Works
Each sticky note is represented by a StickyNote model with the following fields:

- title – short text heading  
- content – main note body  
- author – linked to a Django User  
- date_created – auto-generated timestamp  

Admins can manage users and notes from the Django admin panel.  
All notes are displayed dynamically on the front end, where each note appears in a different color and includes edit and delete options.

---

## Features
-  Create, read, update, and delete sticky notes  
-  Display notes in **different colors** for a fun, visual experience  
-  Each note is assigned to an **author** (managed via the Django admin)  
-  Automatically records date created  
-  Built with **Django’s MVC architecture** (models, views, templates)  
-  Includes **unit tests** for model and view functionality  
-  Fully responsive and easy to run locally  

---

## Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS (separate stylesheet for styling sticky notes)  
- **Database:** SQLite (default Django database)  
- **Testing:** Django’s built-in `TestCase` framework  

---
## Author
Siphokuhle Majozi  
Aspiring software developer and business professional passionate about creating practical, elegant, and user-friendly applications using Django and modern web tools.  
Focused on continuous learning, innovation, and delivering real-world value through technology.
