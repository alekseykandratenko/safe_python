# Why?  
This project was created to study how to ecrypt ML models and create python aplication so it could be safe for a company to send some kind of demos to clients to check the solution
# Use Python 3.12
- pip install numpy scikit-learn joblib nuitka cryptography
# Execution steps in cli
1. Execute model training:
- `python train_model.py`
2. Execute model entriptation. This step create encrypted model and secret key:
- `python encrypt_model.py`
3. Execute script to get secret key and put it into predictor.py:
- `python get_encoded_key.py`
4. Generate executable file:
- Check that all intern tools are installed:
    - `pip install --upgrade setuptools` 
    - `pip install --upgrade nuitka`
    - `pip install --upgrade wheel`
- `nuitka --follow-imports --onefile predictor.py --enable-plugin=numpy --include-package=scipy --include-package=sklearn --include-data-files=model_encrypted.pkl=model_encrypted.pkl`
