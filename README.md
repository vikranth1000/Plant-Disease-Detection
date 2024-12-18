# Plant Disease Classification and Treatment Recommendation

This project focuses on identifying plant diseases using machine learning and deep learning models, integrated with a user-friendly web application. The system predicts the disease from uploaded leaf images and provides specific treatment recommendations to manage or prevent the identified disease.

## Features
- **Disease Prediction**: Supports prediction for multiple plant types (Corn, Potato, and Tomato) with various conditions.
- **Treatment Recommendations**: Provides actionable treatments for identified diseases.
- **User-Friendly Interface**: Built with Flask, allowing users to upload images for instant predictions and recommendations.
- **Model Variants**: Includes multiple pre-trained models (SVC, ANN, CNN, ResNet50) for comparative analysis.

## Models
The project employs several models for disease classification:
- **Support Vector Classifier (SVC)**: For traditional machine learning-based predictions.
- **Artificial Neural Network (ANN)**: A lightweight model for quick predictions.
- **Convolutional Neural Network (CNN)**: For image-based deep learning.
- **ResNet50**: A powerful deep learning model for high accuracy.

## Dataset
The project uses preprocessed datasets of plant leaf images categorized into different diseases and healthy conditions. Data augmentation and preprocessing techniques were applied to enhance model performance.

## Dependencies
The required libraries and dependencies are listed in the `requirements.txt` file. Key dependencies include:
- TensorFlow
- Flask
- NumPy
- Pandas
- Pillow
- Scikit-learn

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

## How to Run
1. Clone the repository and navigate to the project directory.
2. Ensure all required models (`SVC.h5`, `ANN.h5`, `CNN.h5`, `ResNet50.h5`) are available in the `models/` directory.
3. Start the Flask server:
   ```bash
   python app.py
   ```
4. Open a browser and navigate to `http://127.0.0.1:5000/`.
5. Upload a leaf image and select the desired prediction model to view results and recommendations.

## File Structure
- **app.py**: The Flask application code.
- **Plant Disease.ipynb**: Jupyter notebook for model training and experimentation.
- **Accuracy.csv**: Model accuracy comparison data.
- **requirements.txt**: List of required libraries and dependencies.
- **models/**: Directory containing the pre-trained models (`SVC.h5`, `ANN.h5`, `CNN.h5`, `ResNet50.h5`).

## Results
The models achieved varying accuracy levels, as recorded in `Accuracy.csv`. ResNet50 exhibited the highest accuracy, making it the most reliable model for disease prediction.

## Future Enhancements
- Expand dataset to include more plant types and diseases.
- Optimize models for faster predictions.
- Deploy the application to a cloud service for global accessibility.

## Contributors
This project was developed collaboratively as part of a group effort during our undergraduate program.
Collaborators:
M. KRISHNA REVANTH REDDY
J. HEMA SAI VENKAT
B. VENU KUMAR
R. VIKRANTH
B. NAVYA SREE
