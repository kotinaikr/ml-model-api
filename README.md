# Task 1: Housing Price Prediction Model API

A containerized, production-grade REST API that exposes a supervised machine learning regression model to predict housing prices based on structural and environmental features. Built strictly adhering to the specified technical constraints using **Python 3.12+**, **FastAPI**, and **Scikit-learn**.

---

## 🚀 Architectural Walkthrough & Implementation Steps

Here is the structured breakdown of how this microservice was developed from initial repository initialization to containerized execution:

### Phase 1: Repository Architecture & Setup
1. **Directory Isolation:** Initialized the project with a clean directory architecture specifically targeting the isolated `ml-model-api` scope to fulfill the Git delivery constraints.
2. **Dependency Configuration:** Authored `requirements.txt` to pin exact versions of production tools (`fastapi`, `uvicorn`, `scikit-learn`, `pandas`, `joblib`, and `pydantic`).
3. **Git Hygiene:** Set up a comprehensive `.gitignore` filtering out system caches (`__pycache__/`), local virtual environments (`venv/`), environment secrets (`.env`), and decoupling bulky output artifacts (`*.joblib`).

### Phase 2: Data Engineering & Model Training (`train.py`)
1. **Schema Mapping:** Analyzed the structural parameters of the core property files (`TestDataForPrediction.csv`). Isolated seven distinct pricing indicators:
   * `square_footage`, `bedrooms`, `bathrooms`, `year_built`, `lot_size`, `distance_to_city_center`, `school_rating`
2. **Supervised Fit Mechanics:** Leveraged `scikit-learn` to fit an ordinary least squares `LinearRegression` model mapping the core inputs directly to the continuous target output variable (`price`).
3. **Metric Extraction:** Computed performance validation markers, capturing both the **Mean Squared Error (MSE)** and the **$R^2$ (Coefficient of Determination)** score.
4. **Artifact Serialization:** Used `joblib` to securely wrap the trained model instance, feature matrix headers, and structural statistics into a unified deployment artifact (`model.joblib`).

### Phase 3: Production API Layer Architecture (`main.py`)
1. **Dynamic Initialization:** Implemented startup logic to automatically read and reload the binary `model.joblib` into memory immediately upon server ignition.
2. **Strict Validation Schemas:** Utilized Pydantic's `BaseModel` and `Field` constraints to enforce strict data-typing and provide clean structural validation messages for incoming client payloads.
3. **Mandatory Interface Implementations:**
   * **`GET /health`**: Returns the functional operational state of the container and reloaded model validation status.
   * **`GET /model-info`**: Exposes mathematical model coefficients, intercept scalars, and historical training accuracy metrics.
   * **`POST /predict`**: Accepts array collections (`List[HouseFeatures]`), natively facilitating both **single** and **batch** prediction passes through vectorized Pandas calculations.

### Phase 4: Containerization & Isolated Deployment (`Dockerfile`)
1. **Lightweight Base Scaffolding:** Selected the official `python:3.12-slim` image to reduce overhead and minimize security attack surfaces.
2. **Caching Strategy Optimization:** Structured the execution layer to copy and execute `pip install` on the dependency configuration blocks before copying application codes, accelerating sub-sequent image build speeds.
3. **Network Configuration:** Configured internal layer abstractions by exposing application port `8000` and explicitly binding the engine instance across universal interfaces (`0.0.0.0`).

---

## 🛠️ Local Verification & Development Execution

### Running Locally
To install requirements and start the service in a local virtual environment:
```bash
# 1. Initialize and activate environment
python -m venv venv
source venv/Scripts/activate  # Or Windows: venv\Scripts\activate

# 2. Install mapped dependencies
python -m pip install -r requirements.txt

# 3. Train the model and generate the artifact
python train.py

# 4. Fire up the local web engine
python -m uvicorn main:app --reload

