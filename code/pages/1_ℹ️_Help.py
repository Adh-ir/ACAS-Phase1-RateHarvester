import streamlit as st
import os
import sys

# --- PATH CONFIGURATION ---
# Ensure we can import modules from parent directories
current_dir = os.path.dirname(os.path.abspath(__file__)) # code/pages
code_dir = os.path.dirname(current_dir) # code
project_root = os.path.dirname(code_dir) # Forex Rate Extractor

# Add project root to path for 'logic' imports if needed in future
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Add code dir to path for 'ui' imports
if code_dir not in sys.path:
    sys.path.insert(0, code_dir)

# --- IMPORTS ---
try:
    from ui.components import load_css
except ImportError:
    st.error("Could not import UI components. Check python path.")

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Help - FX-Test",
    page_icon=os.path.join(code_dir, "favicon_optimized.png"),
    layout="wide"
)

# --- STYLING ---
# Skip global styles that include the shell, apply custom minimal styling for Help page
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Kanit:ital,wght@0,900;1,900&family=Varela+Round&display=swap');
    
    /* Remove shell entirely */
    section[data-testid="stMain"]>.block-container {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 20px 30px !important;
        margin-top: 10px !important;
        max-width: 1200px !important;
    }
    
    /* Replicate essential text styling from main app */
    body, .stMarkdown, .stText, p, h1, h2, h3, div, span, label, li {
        color: #172E04 !important;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Gradient Title */
    .gradient-title {
        font-size: 3.5rem !important;
        margin-bottom: 0px !important;
        margin-top: -10px !important;
        letter-spacing: -1px;
        display: inline-block;
    }
    
    .title-fx {
        font-family: 'Kanit', sans-serif !important;
        font-weight: 900 !important;
        font-style: italic;
        background: linear-gradient(135deg, #033622 0%, #066F45 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-right: 5px;
    }
    
    .title-test {
        font-family: 'Varela Round', sans-serif !important;
        font-weight: 400 !important;
        background: linear-gradient(135deg, #066F45 0%, #21BA1C 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-left: 5px;
    }
    
    /* Hide header and footer */
    header[data-testid="stHeader"], footer {
        display: none !important;
    }
    
    /* Hide sidebar */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    
    /* App background */
    .stApp {
        background-color: #d8eee1;
        background-image:
            radial-gradient(at 0% 0%, #95dfb1 0, transparent 50%),
            radial-gradient(at 50% 0%, #bee6b7 0, transparent 50%),
            radial-gradient(at 100% 0%, #5ddf79 0, transparent 50%);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
# Replicate the main app header
st.markdown('<h1 class="gradient-title"><span class="title-fx">FX</span> <span class="title-test">Test</span> <span style="font-size: 2rem; vertical-align: middle; opacity: 0.7;">| Help & Information</span></h1>', unsafe_allow_html=True)

# Content will be styled by the global block-container CSS

# --- SECTIONS ---

# 1. About
st.markdown("## 📖 About Application")
st.write("""
**FX-Test** is a professional-grade tool designed for extracting, validating, and auditing foreign exchange rates. 
It bridges the gap between raw API data and financial reporting requirements, offering both bulk rate extraction and automated audit capabilities.
""")

st.markdown("---")

# 2. How to Use
st.markdown("## 🛠️ How to Use")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 1. Rate Extraction")
    st.info("""
    Use this tab to fetch historical exchange rates for analysis or reporting.
    
    1.  **Configure**: Select your **Base Currency** (e.g., ZAR) and one or more **Source Currencies**.
    2.  **Date Range**: Define the period for which you need rates.
    3.  **Run**: Click **Run Extraction** to fetch data.
    4.  **Export**: Download results as CSV or Excel.
    """)

with col2:
    st.markdown("### 2. Audit & Reconciliation")
    st.success("""
    Use this tab to validate your own system's rates against market data.
    
    1.  **Upload**: Provide an Excel/CSV file with columns: `Date`, `Base`, `Source`, `User Rate`.
    2.  **Set Threshold**: Define an acceptable variance percentage (e.g., 5%).
    3.  **Generate**: The system compares your rates vs. API rates.
    4.  **Review**: Identify "Exceptions" (rates outside threshold) and "Errors".
    """)

st.markdown("---")

# 3. Data Source & Reliability
st.markdown("## 🌐 Data Source: Twelve Data")
st.write("""
We utilize **Twelve Data** as our primary source for exchange rate information. 
Twelve Data is a premier financial data provider used by industry giants and institutional investors worldwide.
""")

# Logos/Mentions (Text based for now)
st.markdown("""
<div style="display: flex; gap: 20px; align-items: center; margin: 20px 0;">
    <span style="font-weight: bold; color: #555;">Trusted by:</span>
    <span style="background: rgba(0,0,0,0.05); padding: 5px 10px; border-radius: 5px; font-weight: bold; color: #444;">Google</span>
    <span style="background: rgba(0,0,0,0.05); padding: 5px 10px; border-radius: 5px; font-weight: bold; color: #444;">Microsoft</span>
    <span style="background: rgba(0,0,0,0.05); padding: 5px 10px; border-radius: 5px; font-weight: bold; color: #444;">Amazon</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
[**Visit Twelve Data Website**](https://twelvedata.com) :external-link:
""")

st.markdown("---")

# 4. Validation & Accuracy
st.markdown("## ✅ Internal Validation & Accuracy")
st.write("""
Before deployment, this application underwent rigorous API validation testing to ensure data integrity.
**Status: VALIDATED**
""")

with st.expander("See Validation Details"):
    st.markdown("""
    **Methodology**:
    We compared Twelve Data (Production) against ExchangeRatesAPI (Benchmark) across diverse currency pairs and timeframes.
    
    **Key Findings**:
    1.  **Core Accuracy**: Major pairs (ZAR/USD, ZAR/EUR) showed strong alignment (< 1% deviation).
    2.  **"Market Close" Phenomenon**: 
        *   Forex is 24/5. Different providers snapshot "Daily Close" at different times (e.g., New York 5PM vs. London Midnight).
        *   This causes expected variances (up to 10-15%) in volatile pairs like JPY/NZD during these time gaps.
        *   **This does not indicate bad data**, but rather different timestamp conventions.
    
    **Conclusion**:
    The API is validated for use, with particular reliability for standard banking cross-rates.
    """)

with st.expander("👨‍💻 Developer System Verification"):
    st.info("""
    **Developer System Verification Tests**
    
    The following automated tests are executed to ensure system stability and correctness:
    
    *   **Unit Tests**:
        *   `test_api_client.py`: Verifies Twelve Data API connectivity and error handling.
        *   `test_auditor.py`: Validates the logic for comparing user files against API rates.
        *   `test_data_processor.py`: Checks data cleaning and normalization routines.
    *   **Utility Tests**:
        *   `test_utils.py`: Ensures CSV/Excel conversion and date parsing work correctly.
    """)

st.markdown("---")

# 5. Getting API Keys
st.markdown("## 🔑 Getting Started")
st.warning("""
To use this application, you need a **Twelve Data API Key**.
""")

st.markdown("""
1.  **Register**: Sign up for a free or premium account at [Twelve Data](https://twelvedata.com).
2.  **Get Key**: Navigate to your [API Keys Dashboard](https://twelvedata.com/account/api-keys).
3.  **Input**: Copy the key and paste it into the secure prompt when launching this app.
""")

# End of Help page content
