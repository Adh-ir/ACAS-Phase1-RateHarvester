# Forex Rate Extractor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fxtest.streamlit.app)

A Python-based Streamlit application to extract and audit historical foreign exchange rates using the Twelve Data API.

🌐 **Live App**: [fxtest.streamlit.app](https://fxtest.streamlit.app)

## Features

### 📊 Rate Extraction
*   **Historical Data**: Fetches exchange rates for requested currency pairs and date ranges.
*   **Cross-Rate Calculation**: Automatically calculates cross-rates (e.g., ZAR → BWP) via USD.
*   **Export Options**: Download results as CSV or Excel.

### 🔍 Audit & Reconciliation
*   **Rate Validation**: Upload your own rates file and compare against official Twelve Data API rates.
*   **Flexible Schema**: Supports various column naming conventions (Date, Base, Source, Rate).
*   **Variance Detection**: Marks rates as PASS or EXCEPTION based on configurable threshold.
*   **Testing Mode**: Use mock data to test without consuming API credits.
*   **Smart Rate Limiting**: Respects Twelve Data's free tier limits (8 req/min).

## Quick Start

### Access via Streamlit Cloud (Recommended)
Visit [fxtest.streamlit.app](https://fxtest.streamlit.app) — no installation required!

### Running Locally
```bash
# Clone the repository
git clone https://github.com/Adh-ir/FXtest.git
cd FXtest

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run src/forex/main.py
```

### Running with Docker
```bash
docker-compose up --build
```
**Default URL**: `http://localhost:8501`

## Project Structure

```
FXtest/
├── src/forex/                     # Main Python Package
│   ├── main.py                    # App entry point (Auth, Nav, Page Config)
│   ├── facade.py                  # High-level API for rate fetching
│   ├── auditor.py                 # Audit & reconciliation module
│   ├── api_client.py              # Twelve Data API client with rate limiting
│   ├── data_processor.py          # Data transformation & cross-rate calculation
│   ├── cache.py                   # Cache abstraction (In-memory/Redis)
│   ├── config.py                  # Centralized configuration
│   ├── auth.py                    # API key authentication (cookie-based)
│   ├── utils.py                   # CSV/Excel export helpers
│   ├── a11y_checker.py            # Accessibility validation
│   ├── ui/                        # UI Layer
│   │   ├── tabs/                  # Tab modules
│   │   │   ├── extraction.py      # Rate Extraction tab
│   │   │   └── audit.py           # Audit & Reconciliation tab
│   │   ├── components.py          # Reusable Streamlit components
│   │   └── styles.css             # Custom CSS styling
│   └── assets/                    # Static assets (favicon, etc.)
│
├── tests/                         # Test Suite
│   ├── conftest.py                # Pytest fixtures and configuration
│   ├── test_api_client.py         # API client tests
│   ├── test_auditor.py            # Auditor module tests
│   ├── test_data_processor.py     # Data processor tests
│   ├── test_facade.py             # Facade tests
│   ├── test_main.py               # Main app tests
│   ├── test_utils.py              # Utility function tests
│   ├── test_accessibility.py      # Accessibility tests
│   ├── test_enhancements.py       # Enhancement tests
│   └── test_redis_integration.py  # Redis integration tests
│
├── .github/workflows/             # CI/CD Pipeline
├── Dockerfile                     # Container definition
├── docker-compose.yml             # Container orchestration (app + Redis)
├── pyproject.toml                 # Project configuration
├── requirements.txt               # Python dependencies
├── requirements-test.txt          # Test dependencies
├── CONTRIBUTING.md                # Contribution guidelines
├── RUNBOOK.md                     # Disaster recovery runbook
└── README.md                      # This file
```

### High-Level Architecture

```mermaid
graph TD
    User([User]) <--> UI[Streamlit UI<br>src/forex/main.py]
    UI --> Facade[Logic Facade<br>src/forex/facade.py]
    
    subgraph "Business Logic Layer"
        Facade --> Auditor[Auditor Module]
        Facade --> Client[API Client<br>src/forex/api_client.py]
        Auditor --> Client
    end
    
    subgraph "Infrastructure"
        Facade --> Cache[Cache<br>Redis/Memory]
        Client --> Config[Centralized Config]
    end
    
    Client -- "HTTPS (Rate Limited)" --> TwelveData[((Twelve Data API))]
    
    classDef component fill:#d4ebf2,stroke:#005580,stroke-width:1px;
    class UI,Facade,Auditor,Client,Cache component;
```

## Usage

### Rate Extraction
1. Enter base and source currencies (e.g., ZAR, USD)
2. Select date range
3. Click "Run Extraction"

### Audit & Reconciliation
1. Switch to the "Audit & Reconciliation" tab
2. Upload your Excel/CSV file with columns: Date, Base, Source, User Rate
3. Configure date format and variance threshold
4. Enable "Testing Mode" for initial testing (recommended)
5. Click "Generate Audit"

## Configuration

### API Key Setup
1. Sign up at [Twelve Data](https://twelvedata.com/) (Free tier available)
2. Copy your API key
3. Enter the key in the application's authentication dialog

### Environment Variables (Optional)
Create a `.env` file for local development:
```bash
TWELVEDATA_API_KEY=your_api_key_here
REDIS_URL=redis://localhost:6379  # Optional: for Redis caching
```

## Security

- API keys are stored in **browser cookies** (7-day expiry)
- No API keys are saved on the server
- `.env` files are gitignored
- HTTPS enforced on Streamlit Cloud

## API Rate Limits (Twelve Data Free Tier)

- 8 API calls per minute
- 800 API calls per day

The application implements smart throttling to respect these limits.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and coding standards.

### Running Tests
```bash
# Full test suite
pytest

# With coverage
pytest --cov=forex tests/

# Skip integration tests
pytest -m "not integration"
```

## Dependencies

| Package | Purpose |
|---------|---------|
| streamlit | Web application framework |
| pandas | Data manipulation |
| openpyxl | Excel file support |
| requests | HTTP client |
| extra-streamlit-components | Cookie management |
| watchdog | File system monitoring |

## License

This project is for internal use only. See LICENSE for details.

---

**Repository**: [github.com/Adh-ir/FXtest](https://github.com/Adh-ir/FXtest)  
**Live App**: [fxtest.streamlit.app](https://fxtest.streamlit.app)
