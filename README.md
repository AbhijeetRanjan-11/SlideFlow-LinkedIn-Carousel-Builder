🖼️ LinkedIn Carousel Generator — Full Project Overview

The LinkedIn Carousel Generator is a Python-based desktop application designed to simplify the creation of professional, branded carousels in PDF format. Whether you're crafting content for LinkedIn, Instagram, or personal branding, this tool lets you generate consistent, square-format slides with minimal effort — all without needing complex design software.
🎯 Purpose & Use Case

This project addresses the growing demand for visual storytelling on platforms like LinkedIn, where multi-slide PDF carousels improve engagement, communicate ideas, and promote personal or business brands effectively.

Instead of relying on tools like Canva or Photoshop, this generator provides a quick, no-code solution to produce ready-to-upload carousel posts with your branding, images, and custom styles.
⚙️ Key Functionalities

✔️ Slide Content Creation:

    Enter custom text for each slide (centered by default)

    Supports unlimited slides

✔️ Color Customization:

    Define background color for each slide using HEX codes (e.g., #FFFFFF for white)

    Choose text color separately for better readability

✔️ Background Image Support:

    Optionally set an image as the slide background

    Automatically resized to 1080x1080 pixels

✔️ Profile Branding:

    Add a profile picture displayed on each slide

    Enter your name or handle to appear beside the profile image

✔️ Export to PDF:

    One-click PDF export with square slide dimensions (1080x1080)

    Each slide appears on a new page

    Optimized for LinkedIn, Instagram, and similar platforms

✔️ Graphical User Interface (GUI):

    Built with Tkinter for simplicity and ease of use

    File dialogs for selecting images and export paths

    Interactive color and text inputs

🛠️ Technology Stack

| Technology       | Role                         |
| ---------------- | ---------------------------- |
| **Python 3.x**   | Core programming language    |
| **Tkinter**      | GUI development framework    |
| **Pillow (PIL)** | Image processing & resizing  |
| **ReportLab**    | PDF generation engine        |
| **OS module**    | File path & existence checks |


📂 How the Code Works
1️⃣ Slide Management

    Users input text, background color, text color, and optionally a background image

    Each slide's settings are stored in a list as a dictionary

2️⃣ Profile Branding

    Users can upload a profile picture shown on all slides

    A profile name or handle can be added, positioned near the profile image

3️⃣ PDF Generation

    Iterates through stored slides

    For each slide:
    ➤ If a background image exists, it's placed full-size (1080x1080)
    ➤ Otherwise, a solid background color fills the slide
    ➤ Text is placed centrally with chosen color
    ➤ Profile image and name (if provided) are positioned near the bottom

    Final output is a multi-page PDF, each page representing a single slide



🖥️ GUI Preview

Simple, user-friendly interface built with Tkinter:

+-------------------------------------+
| Slide Text Input Area               |
+-------------------------------------+
| Background Color (Hex)              |
| Text Color (Hex)                    |
| [Choose Background Image]           |
| [Set Profile Image] [Set Name]      |
| [Add Slide] [Export to PDF]         |
+-------------------------------------+

Each slide is generated with:

    1080 x 1080 resolution (LinkedIn/Instagram standard)

    Centered text content

    Optional background image or solid color

    Optional profile branding


▶️ Run the Application

python carousel_generator.py

💡 Example Use Cases

✅ LinkedIn PDF Carousels for professional posts
✅ Instagram or Facebook square image posts
✅ Marketing materials with consistent design
✅ Content creation with personalized branding

🛡️ Notes

    Ensure selected images (background or profile) are .jpg, .jpeg, or .png

    Hex codes for colors should follow the format: #RRGGBB

    Slides are exported as a single .pdf file with one slide per page

🎯 Future Improvements (Optional Ideas)

    Font selection options

    Font size customization

    Multiple text positioning options

    Preview mode before export

    Dark mode UI



This project is provided for educational and personal use. Customize and extend as needed for your projects.

Create professional, branded carousels in minutes with this lightweight, Python-powered tool! 🎨📢
