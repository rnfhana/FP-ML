import streamlit as st
import base64
from pathlib import Path

def load_css():
    """Load custom CSS styling"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        font-weight: 300;
        margin: 0;
    }
    
    /* Sidebar Styling */
    .sidebar-header {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sidebar-header h2 {
        color: white;
        margin: 0;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Page Headers */
    .page-header {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .page-header h2 {
        color: #2c3e50;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .page-header p {
        color: #5a6c7d;
        font-size: 1.1rem;
        margin: 0;
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        border-left: 4px solid #667eea;
    }
    
    .feature-card h2, .feature-card h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .feature-card p {
        color: #5a6c7d;
        line-height: 1.6;
    }
    
    /* Waste Categories */
    .waste-categories {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .category-item {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        color: white;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Features Grid */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .feature-item {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .feature-item h4 {
        color: #2c3e50;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .feature-item p {
        color: #5a6c7d;
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* Stats Card */
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
    }
    
    .stats-card h3 {
        text-align: center;
        margin-bottom: 1.5rem;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    .stat-item {
        text-align: center;
        margin-bottom: 1rem;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        backdrop-filter: blur(10px);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.8;
        font-weight: 300;
    }
    
    /* Guide Card */
    .guide-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1.5rem;
    }
    
    .guide-card h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .guide-card ol {
        color: #5a6c7d;
        padding-left: 1rem;
    }
    
    .guide-card li {
        margin-bottom: 0.5rem;
        line-height: 1.5;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    
    .info-box h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .info-box p {
        color: #5a6c7d;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
    }
    
    /* Section Headers */
    .section-header {
        text-align: center;
        margin: 2rem 0 1rem 0;
    }
    
    .section-header h3 {
        color: #2c3e50;
        font-size: 1.5rem;
        font-weight: 600;
    }
    
    /* Upload Section */
    .upload-section {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .upload-section h3 {
        color: white;
        margin: 0;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Results Section */
    .results-section {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .results-section h3 {
        color: white;
        margin: 0;
        font-weight: 600;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Prediction Card */
    .prediction-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    
    .prediction-main h2 {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .confidence-score {
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        backdrop-filter: blur(10px);
    }
    
    .confidence-score span {
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    /* Recommendation Card */
    .recommendation-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1rem;
    }
    
    .recommendation-card h4 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .recommendation-card p, .recommendation-card ul {
        color: #5a6c7d;
        line-height: 1.6;
    }
    
    .recommendation-card li {
        margin-bottom: 0.5rem;
    }
    
    /* Insight Cards */
    .insight-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
        height: 100%;
    }
    
    .insight-card h4 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .insight-card p {
        color: #5a6c7d;
        line-height: 1.6;
        margin: 0;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .main-header p {
            font-size: 1rem;
        }
        
        .page-header h2 {
            font-size: 1.5rem;
        }
        
        .features-grid {
            grid-template-columns: 1fr;
        }
        
        .waste-categories {
            grid-template-columns: 1fr;
        }
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Metric Styling */
    [data-testid="metric-container"] {
        background: white;
        border: 1px solid #e1e8ed;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* File Uploader Styling */
    .stFileUploader {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        border: 2px dashed #667eea;
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        background: white;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

def get_waste_emoji(waste_type):
    """Get emoji for waste type"""
    emoji_map = {
        'cardboard': '♻️',
        'metal': '🔩',
        'paper': '📄',
        'plastic': '🥤',
        'glass': '🍶'
    }
    return emoji_map.get(waste_type.lower(), '🗑️')

def get_disposal_recommendations(waste_type):
    """Get disposal recommendations for each waste type"""
    recommendations = {
        'cardboard': """
            <h4>♻️ Cardboard Disposal</h4>
            <p><strong>Recycling Instructions:</strong></p>
            <ul>
                <li>Remove all tape, labels, and staples</li>
                <li>Flatten boxes to save space</li>
                <li>Keep dry - wet cardboard can't be recycled</li>
                <li>Place in recycling bin or take to recycling center</li>
            </ul>
            <p><strong>Environmental Impact:</strong> Recycling cardboard saves trees and reduces landfill waste.</p>
        """,
        'metal': """
            <h4>🔩 Metal Disposal</h4>
            <p><strong>Recycling Instructions:</strong></p>
            <ul>
                <li>Clean containers to remove food residue</li>
                <li>Remove labels when possible</li>
                <li>Separate aluminum from steel if required</li>
                <li>Place in recycling bin or scrap metal collection</li>
            </ul>
            <p><strong>Environmental Impact:</strong> Metal recycling saves energy and natural resources significantly.</p>
        """,
        'paper': """
            <h4>📄 Paper Disposal</h4>
            <p><strong>Recycling Instructions:</strong></p>
            <ul>
                <li>Remove plastic windows from envelopes</li>
                <li>Keep paper clean and dry</li>
                <li>Separate different types (newspaper, office paper, etc.)</li>
                <li>Place in paper recycling bin</li>
            </ul>
            <p><strong>Environmental Impact:</strong> Paper recycling reduces deforestation and saves water.</p>
        """,
        'plastic': """
            <h4>🥤 Plastic Disposal</h4>
            <p><strong>Recycling Instructions:</strong></p>
            <ul>
                <li>Check recycling number (1-7) on container</li>
                <li>Rinse containers to remove food residue</li>
                <li>Remove caps and lids if required</li>
                <li>Place in appropriate recycling bin</li>
            </ul>
            <p><strong>Environmental Impact:</strong> Plastic recycling reduces ocean pollution and landfill waste.</p>
        """,
        'glass': """
            <h4>🍶 Glass Disposal</h4>
            <p><strong>Recycling Instructions:</strong></p>
            <ul>
                <li>Rinse containers to remove residue</li>
                <li>Remove metal lids and caps</li>
                <li>Separate by color if required (clear, brown, green)</li>
                <li>Place in glass recycling bin</li>
            </ul>
            <p><strong>Environmental Impact:</strong> Glass can be recycled infinitely without quality loss.</p>
        """
    }
    return recommendations.get(waste_type.lower(), """
        <h4>🗑️ General Waste Disposal</h4>
        <p>Please follow local waste disposal guidelines for proper handling.</p>
    """)

def format_probability(prob):
    """Format probability as percentage"""
    return f"{prob:.1%}"

def get_confidence_color(confidence):
    """Get color based on confidence level"""
    if confidence >= 0.8:
        return "green"
    elif confidence >= 0.6:
        return "orange"
    else:
        return "red"

def create_download_link(data, filename, text):
    """Create a download link for data"""
    if isinstance(data, str):
        data = data.encode()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text}</a>'
    return href

def validate_image(image):
    """Validate uploaded image"""
    if image is None:
        return False, "No image uploaded"
    
    # Check file size (limit to 10MB)
    if hasattr(image, 'size') and image.size > 10 * 1024 * 1024:
        return False, "Image too large (max 10MB)"
    
    # Check image format
    try:
        from PIL import Image
        img = Image.open(image)
        if img.format not in ['JPEG', 'PNG', 'JPG']:
            return False, "Unsupported format (use JPEG/PNG)"
        return True, "Valid image"
    except Exception as e:
        return False, f"Invalid image: {str(e)}"

def resize_image(image, max_size=(800, 600)):
    """Resize image while maintaining aspect ratio"""
    try:
        from PIL import Image
        
        # Calculate new size maintaining aspect ratio
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        return image
    except Exception as e:
        print(f"Error resizing image: {str(e)}")
        return image

def get_image_info(image):
    """Get image information"""
    try:
        info = {
            'format': image.format,
            'mode': image.mode,
            'size': image.size,
            'width': image.width,
            'height': image.height
        }
        return info
    except Exception as e:
        return {'error': str(e)}