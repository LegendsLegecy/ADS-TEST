# AdMonetized Flask App

A simple Flask application designed to display ads using Adsterra for monetization, optimized for deployment on Vercel.

## Features

- 🎯 **Adsterra Integration**: Multiple ad placements (banner, sidebar, in-content)
- 📱 **Responsive Design**: Mobile-optimized with Bootstrap 5
- 🚀 **Vercel Ready**: Pre-configured for easy deployment
- 💰 **Revenue Tracking**: Built-in analytics and revenue simulation
- 🎨 **Modern UI**: Clean, professional design with Font Awesome icons

## Ad Placements

The app includes strategic ad placements for maximum revenue:

1. **Top Banner Ads**: Above the main content
2. **Sidebar Ads**: Right-side vertical ads
3. **In-Content Ads**: Between article sections
4. **Bottom Banner Ads**: Below main content

## Setup Instructions

### 1. Get Your Adsterra Publisher ID

1. Sign up at [Adsterra.com](https://www.adsterra.com)
2. Complete the publisher verification process
3. Get your Publisher ID from the dashboard

### 2. Local Development

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Adsterra Publisher ID:
   ```bash
   export ADSTERRA_PUBLISHER_ID="your_publisher_id_here"
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open http://localhost:5000 in your browser

### 3. Deploy to Vercel

#### Option A: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy:
   ```bash
   vercel
   ```

4. Set environment variable:
   ```bash
   vercel env add ADSTERRA_PUBLISHER_ID
   # Enter your Adsterra Publisher ID when prompted
   ```

#### Option B: Deploy via Vercel Dashboard

1. Push your code to GitHub
2. Go to [Vercel Dashboard](https://vercel.com/dashboard)
3. Click "New Project"
4. Import your GitHub repository
5. Add environment variable:
   - Name: `ADSTERRA_PUBLISHER_ID`
   - Value: Your Adsterra Publisher ID
6. Click "Deploy"

## Environment Variables

- `ADSTERRA_PUBLISHER_ID`: Your Adsterra publisher ID (required)

## File Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── README.md             # This file
└── templates/
    ├── base.html         # Base template with navigation and footer
    ├── index.html        # Home page with ads
    ├── about.html        # About page with ads
    └── contact.html      # Contact page with ads
```

## Adsterra Integration

The app uses Adsterra's JavaScript integration method:

```javascript
var adsterra_pub = 'YOUR_PUBLISHER_ID';
var adsterra_type = '2';
var adsterra_sid = 'unique_ad_id';
```

Each ad placement has a unique `adsterra_sid` to track performance individually.

## Customization

### Adding More Pages

1. Add a new route in `app.py`:
   ```python
   @app.route('/new-page')
   def new_page():
       return render_template('new_page.html', publisher_id=ADSTERRA_PUBLISHER_ID)
   ```

2. Create a new template in `templates/new_page.html`:
   ```html
   {% extends "base.html" %}
   {% block content %}
   <!-- Your content here -->
   {% endblock %}
   ```

### Modifying Ad Placements

Edit the HTML templates to add, remove, or reposition ad containers. Each ad needs:
- A unique `id` attribute
- A unique `adsterra_sid` in the script
- The Adsterra script loading code

### Styling

The app uses Bootstrap 5 and custom CSS. Modify the styles in `templates/base.html` or add your own CSS files.

## Revenue Optimization Tips

1. **Placement**: Position ads where users naturally look
2. **Mobile**: Ensure ads are mobile-friendly
3. **Loading**: Use async loading to prevent page slowdown
4. **Testing**: A/B test different ad placements
5. **Content**: Create engaging content to increase page views

## Support

For technical support or questions about this app, please contact us through the contact page or create an issue in the repository.

For Adsterra-specific questions, contact [Adsterra Support](https://www.adsterra.com/support).

## License

This project is open source and available under the MIT License.
