# Edge AI Prototype

- Tools: TensorFlow Lite, Raspberry Pi/Colab (simulation).
- Goal:
1. Train a lightweight image classification model (e.g., recognizing recyclable items).
2. Convert the model to TensorFlow Lite and test it on a sample dataset.
3. Explain how Edge AI benefits real-time applications.

**Summary**
*Data Source*: [Trash type image dataset](https://www.kaggle.com/datasets/farzadnekouei/trash-type-image-dataset)
*Preprocessing*: All images were resized to 128×128, and normalized. Dropout of 0.5 was applied to prevent overfitting.
*Model architecture*: CNN was used to classifiy images into various classes.
*Conversion*: TFLite model was converted so that it can run on device.
*Evaluation*: The model achieved an accuracy of 69% having trained the data on 10 epochs.
*Deployment*: This app could be deployed on Streamlit to perform the task on real-time.

