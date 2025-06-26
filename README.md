# SlideFlow-LinkedIn-Carousel-Builder

🎨 LinkedIn Carousel Generator (Python + Tkinter)

A simple desktop application to generate PDF-based LinkedIn Carousels with customizable slides, background colors, images, text colors, and optional profile branding — perfect for building engaging content for LinkedIn carousels, Instagram posts, or other social platforms.
🚀 Features

✅ Create visually appealing carousel slides with custom text
✅ Set background colors or choose an image for each slide
✅ Customize text color for better visual contrast
✅ Add a profile image and your name/handle as a footer on each slide
✅ One-click PDF export with standard 1080x1080 dimensions (LinkedIn/Instagram optimized)
✅ Built using Tkinter for the GUI, Pillow for image processing, and ReportLab for PDF generation

🛠️ Technologies Used

    Python 3.x

    Tkinter - GUI framework

    Pillow - Image handling

    ReportLab - PDF generation

    os - File handling

📦 How It Works

    Enter Slide Text: Add the main text for your slide.

    Customize Colors: Define background and text colors using Hex codes.

    Optional Background Image: Choose an image to be used as the slide background.

    Profile Branding (Optional):

        Add a profile picture (displayed on each slide)

        Enter your name or handle (shown beside the profile image)

    Add Slide: Save the current slide to your carousel sequence.

    Export to PDF: Generate a professional PDF with all slides, ready to share!

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

📂 Project Structure

carousel_generator.py  # Main Python script with GUI and PDF logic

📥 Requirements

    Python 3.x

    Libraries:

    pip install pillow reportlab

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
