import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
from io import BytesIO
import time

# Import custom modules
from model_handler import ModelHandler
from utils import *

# Page config
st.set_page_config(
    page_title="🗂️ Smart Waste Classifier",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Initialize model handler
@st.cache_resource
def load_model():
    return ModelHandler()

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>♻️ Smart Waste Classifier</h1>
        <p>AI-Powered Waste Classification System using Deep Learning</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-header">
            <h2>🔧 Control Panel</h2>
        </div>
        """, unsafe_allow_html=True)
        
        page = st.selectbox(
            "Select Page",
            ["🏠 Home", "📊 Model Analytics", "🔍 Image Classifier"],
            index=0
        )
        
        st.markdown("---")
        
        # Model info
        st.markdown("""
        <div class="info-box">
            <h3>Model Information</h3>
            <p><strong>Architecture:</strong> ResNet34</p>
            <p><strong>Classes:</strong> 5 waste types</p>
            <p><strong>Training:</strong> 15 epochs</p>
            <p><strong>Input Size:</strong> 224x224</p>
        </div>
        """, unsafe_allow_html=True)

    # Main content
    if page == "🏠 Home":
        show_home_page()
    elif page == "📊 Model Analytics":
        show_analytics_page()
    elif page == "🔍 Image Classifier":
        show_classifier_page()

def show_home_page():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h2>🎯 About This Application</h2>
            <p>This application uses a deep learning model based on ResNet34 architecture to classify waste images into 5 categories:</p>
            <div class="waste-categories">
                <div class="category-item">♻️ <strong>Cardboard</strong></div>
                <div class="category-item">🔩 <strong>Metal</strong></div>
                <div class="category-item">📄 <strong>Paper</strong></div>
                <div class="category-item">🥤 <strong>Plastic</strong></div>
                <div class="category-item">🍶 <strong>Glass</strong></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Key Features
        st.markdown("""
        <div class="feature-card">
            <h3>✨ Key Features</h3>
            <div class="features-grid">
                <div class="feature-item">
                    <h4>🚀 Real-time Classification</h4>
                    <p>Upload images and get instant predictions with confidence scores</p>
                </div>
                <div class="feature-item">
                    <h4>📊 Detailed Analytics</h4>
                    <p>Comprehensive model performance metrics and visualizations</p>
                </div>
                <div class="feature-item">
                    <h4>🎨 Interactive Interface</h4>
                    <p>User-friendly design with professional charts and graphs</p>
                </div>
                <div class="feature-item">
                    <h4>⚡ Fast Processing</h4>
                    <p>Optimized model inference for quick results</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-card">
            <h3>📈 Model Statistics</h3>
            <div class="stat-item">
                <div class="stat-number">95.2%</div>
                <div class="stat-label">Accuracy</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">0.94</div>
                <div class="stat-label">F1 Score</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">5</div>
                <div class="stat-label">Categories</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">ResNet34</div>
                <div class="stat-label">Architecture</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick start guide
        st.markdown("""
        <div class="guide-card">
            <h3>🚀 Quick Start</h3>
            <ol>
                <li>Navigate to <strong>Image Classifier</strong></li>
                <li>Upload or take a waste image</li>
                <li>Click <strong>Classify</strong></li>
                <li>View results and confidence scores</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

def show_analytics_page():
    st.markdown("""
    <div class="page-header">
        <h2>📊 Model Analytics Dashboard</h2>
        <p>Comprehensive analysis of model performance and data distribution</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data for demonstration (in real app, this would come from actual model training)
    waste_types = ['Cardboard', 'Metal', 'Paper', 'Plastic', 'Glass']
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Class distribution
        class_counts = [450, 380, 420, 500, 340]
        fig_dist = px.pie(
            values=class_counts,
            names=waste_types,
            title="Training Data Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_dist.update_traces(textposition='inside', textinfo='percent+label')
        fig_dist.update_layout(
            title_font_size=16,
            showlegend=True,
            height=400
        )
        st.plotly_chart(fig_dist, use_container_width=True)
    
    with col2:
        # Training metrics
        epochs = list(range(1, 16))
        train_loss = [2.193717, 1.366992, .877479, .702801, .556583, .480097, .390006, .351450, .279111, .233574, .239484, .206978, .186734, .179095, .163392]
        val_loss = [.988774, .463428, .424647, .386357, .339549, .326315, .294419, .301346, .249734, .259495, .242540, .225420, .215690, .213206, .218940]
        
        fig_loss = go.Figure()
        fig_loss.add_trace(go.Scatter(x=epochs, y=train_loss, mode='lines+markers', name='Training Loss', line=dict(color='#ff6b6b')))
        fig_loss.add_trace(go.Scatter(x=epochs, y=val_loss, mode='lines+markers', name='Validation Loss', line=dict(color='#4ecdc4')))
        fig_loss.update_layout(
            title="Training & Validation Loss",
            xaxis_title="Epoch",
            yaxis_title="Loss",
            height=400,
            title_font_size=16
        )
        st.plotly_chart(fig_loss, use_container_width=True)
    
    # Confusion Matrix
    st.markdown("""
    <div class="section-header">
        <h3>🎯 Model Performance Matrix</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Sample confusion matrix data
    confusion_data = np.array([
        [35, 0, 1, 2, 2],
        [0, 43, 3, 0, 4],
        [0, 0, 41, 0, 0],
        [0, 0, 0, 58, 1],
        [0, 4, 1, 0, 43]
    ])
    
    fig_cm = px.imshow(
        confusion_data,
        labels=dict(x="Predicted", y="Actual", color="Count"),
        x=waste_types,
        y=waste_types,
        color_continuous_scale="Blues",
        title="Confusion Matrix"
    )
    
    # Add text annotations
    for i in range(len(waste_types)):
        for j in range(len(waste_types)):
            fig_cm.add_annotation(
                x=j, y=i,
                text=str(confusion_data[i][j]),
                showarrow=False,
                font=dict(color="white" if confusion_data[i][j] > 50 else "black")
            )
    
    fig_cm.update_layout(height=500, title_font_size=16)
    st.plotly_chart(fig_cm, use_container_width=True)
    
    # Performance metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Overall Accuracy", "92.98%")
    with col2:
        st.metric("Precision", "94.8%")
    with col3:
        st.metric("Recall", "95.1%")
    with col4:
        st.metric("F1 Score", "92.97%")

# Helper function to clear previous results when a new image is provided
def clear_all_results():
    """A callback to clear image and prediction data from session_state."""
    keys_to_clear = ['image_buffer', 'prediction', 'probabilities']
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]

def show_classifier_page():
    st.markdown("""
    <div class="page-header">
        <h2>🔍 Waste Image Classifier</h2>
        <p>Upload an image to classify the type of waste using AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load model
    try:
        model_handler = load_model()
        model_loaded = True
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.info("Please ensure 'my_model.pkl' is in the correct directory.")
        model_loaded = False
        return
    
    col1, col2 = st.columns([1, 1])
    
    def show_classifier_page():
        st.markdown("""
    <div class="page-header">
        <h2>🔍 Waste Image Classifier</h2>
        <p>Upload an image or use your camera to classify the type of waste using AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load model
    try:
        model_handler = load_model()
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.info("Please ensure 'my_model.pkl' is in the correct directory.")
        return
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        tab1, tab2 = st.tabs(["📁 Upload Image", "📸 Use Camera"])

        with tab1:
            uploaded_file = st.file_uploader(
                "Choose Image File",
                type=['png', 'jpg', 'jpeg'],
                help="Format: PNG, JPG, JPEG",
                # Callback ini akan menghapus hasil lama saat file baru dipilih
                on_change=clear_all_results
            )
            if uploaded_file is not None:
                st.session_state.image_buffer = uploaded_file

        with tab2:
            camera_file = st.camera_input(
                "Take a Waste Image",
                # Callback ini akan menghapus hasil lama saat foto baru diambil
                on_change=clear_all_results
            )
            if camera_file is not None:
                st.session_state.image_buffer = camera_file
        
        # Logika terpusat untuk menampilkan gambar dan tombol klasifikasi
        if 'image_buffer' in st.session_state:
            image = Image.open(st.session_state.image_buffer)
            st.image(image, caption="Image for Classification", use_column_width=True)
            
            if st.button("🔍 Image Classification", type="primary", use_container_width=True):
                with st.spinner("🤖 Analyzing Image..."):
                    time.sleep(1)
                    try:
                        # Lakukan prediksi menggunakan gambar dari buffer
                        prediction, probabilities = model_handler.predict(image)
                        
                        # Simpan hasil prediksi di session_state
                        st.session_state.prediction = prediction
                        st.session_state.probabilities = probabilities
                        
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

    # Kolom hasil tidak perlu diubah. Ia akan kosong secara otomatis
    # karena `clear_all_results` menghapus 'prediction' dari session_state.
    
    with col2:
        if hasattr(st.session_state, 'prediction') and st.session_state.prediction:
            st.markdown("""
            <div class="results-section">
                <h3>🎯 Classification Results</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Main prediction
            prediction = st.session_state.prediction
            probabilities = st.session_state.probabilities
            
            # Get confidence score
            max_prob = max(probabilities.values())
            
            st.markdown(f"""
            <div class="prediction-card">
                <div class="prediction-main">
                    <h2>{get_waste_emoji(prediction)} {prediction.upper()}</h2>
                    <div class="confidence-score">
                        <span>Confidence: {max_prob:.1%}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Probability distribution
            st.markdown("### 📊 Probability Distribution")
            
            prob_df = pd.DataFrame(
                list(probabilities.items()),
                columns=['Category', 'Probability']
            )
            prob_df = prob_df.sort_values('Probability', ascending=True)
            
            fig_prob = px.bar(
                prob_df,
                x='Probability',
                y='Category',
                orientation='h',
                color='Probability',
                color_continuous_scale='Viridis',
                title="Confidence Scores for All Categories"
            )
            fig_prob.update_layout(
                height=300,
                showlegend=False,
                title_font_size=14
            )
            fig_prob.update_traces(texttemplate='%{x:.1%}', textposition='outside')
            
            st.plotly_chart(fig_prob, use_container_width=True)
            
            # Disposal recommendations
            st.markdown("### ♻️ Disposal Recommendations")
            recommendations = get_disposal_recommendations(prediction)
            st.markdown(f"""
            <div class="recommendation-card">
                {recommendations}
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()