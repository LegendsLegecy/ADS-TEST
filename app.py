from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Adsterra configuration
ADSTERRA_PUBLISHER_ID = os.environ.get('ADSTERRA_PUBLISHER_ID', 'your_publisher_id_here')

@app.route('/')
def index():
    """Main page with ads"""
    return render_template('index.html', publisher_id=ADSTERRA_PUBLISHER_ID)

@app.route('/about')
def about():
    """About page with ads"""
    return render_template('about.html', publisher_id=ADSTERRA_PUBLISHER_ID)

@app.route('/contact')
def contact():
    """Contact page with ads"""
    return render_template('contact.html', publisher_id=ADSTERRA_PUBLISHER_ID)

@app.route('/api/visitor-count')
def visitor_count():
    """API endpoint for visitor tracking (can be used for analytics)"""
    # This is a simple example - in production you'd use a database
    return jsonify({'visitors': 1234, 'page_views': 5678})

if __name__ == '__main__':
    app.run(debug=True)
