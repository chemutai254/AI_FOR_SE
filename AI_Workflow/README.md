# AI Development Workflow

## Part 1: Short Answer Questions (30 points)

### 1. Problem Definition (6 points)

**Define a hypothetical AI problem**
*AI-powered Crop Disease Detection Application*
- Develop an AI model that analyzes images of crop to detect early signs of disease and alert farmers before significant damage occurs.

**List 3 objectives and 2 stakeholders**
*Objectives*
- Accurately identify crop diseases from leaf images with minimal false positives.

- Provide early warnings to farmers to reduce crop loss and improve yield.

- Offer actionable recommendations (e.g., treatment steps, severity level) through the app.

*Stakeholders*
- Farmers using the application to protect their crops.

- Agricultural extension officers who support farmers and use insights for planning interventions.

**Key Performance Indicator (KPI) to measure success**
- Accuracy Detection Rate (%) — the percentage of correctly identified diseased and healthy crops.

### 2. Data Collection & Preprocessing (8 points)
**Identify 2 data sources for your problem**
1. *Kaggle* [Plant Disease Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease?utm_source=chatgpt.com)
2. *Tensorflow* Datasets Catalog [Plant Village Dataset](https://www.tensorflow.org/datasets/catalog/plant_village?utm_source=chatgpt.com)

**Explain 1 potential bias in the data**
- The AI model may perform well during testing but poorly in real-world scenarios, since the Plant Village Dataset contain high-quality, studio-like images taken under ideal lighting and uniform backgrounds. 
- However, farmers images may contain the following characteristics: **poor lighting**, **blurry or partial leaves**, **complex backgrounds**, **multiple leaves in one photo**, or **dust, shadows, or weather effects**.

**Outline 3 preprocessing steps**
1. *Image Cleaning and Normalization*
- Resize all images to a consistent dimension (224).
- Normalize pixel values (from a scale of 0–255 to 0–1).
- Remove noisy or corrupted images.

2. *Data Augmentation*
- Apply transformations such as rotation, zoom, flip, brightness adjustment.

3. *Label Verification and Class Balancing*
- Ensure labels are correct and consistent across datasets.
- Address class imbalance by oversampling minority classes or using augmentation.

### 3. Model Development (8 points)
1. Choose a model and justify your choice.
- The project utilizes Convolutional Neural Networks (CNN) with transfer learning (the use of pre-trained models) such as **MobileNetV2** and **EfficientNet-lite**.
- Why CNN with transfer learning? This is because CNNs are used in processing images. Transfer learning reduces data needs since it already knows the important visual features capitalizing on speed of crop classification. Additionaly, the two pre-trained models are small and fast, thus can run inference on farmers' mobile devices (offline capability).
2. Describe how you would split data into training/validation/test sets.
- The dataset can be imbalanced due to some rare crop diseases. Thus, stratified splitting would be the best to split the dataset into the same proportion of each disease class. 
3. Name 2 hyperparameters you would tune and why.
- *Learning Rate*: It helps the model converge efficiently. High learning rate may cause unstable training, while low learning rate may slow the training.
- *Dropout Rate*: Dropout helps reduce overfitting by randomly dropping neurons during training. This works efficiently when the dataset is small or the dataset contains imbalanced classes. 
- *Batch Size*: This impacts the gradient stability and memory usage. Small batches give noisy gradients (may generalize better) while large batches train faster but may overfit.
- *Epochs*: The number of epochs controls how long the model is going to train. Too many epochs may lead to overfitting while few epochs, underfitting. Introduce early stopping when the validation loss starts increasing to capture the best performing model and prevent overfitting.
- *Optimizer*: The use of Adam leads to fast training. On the other hand, SGD with momentum often yields better final accuracy. This, different optimizers lead to different convergence behaviors.

### 4. Evaluation & Deployment (8 points)

1. Select 2 evaluation metrics and explain their relevance.
- *Precision*: This measures how many predicted diseased leaves are truly diseased. It helps farmers gain trust on the outcome due to reduced false alert. 
- *F1-Score*: It is useful in imbalanced datasets where some crop diseases are rare.

2. What is concept drift? How would you monitor it post-deployment?
- *Concept drift* occurs when the statistical properties of the target variable, or the relationship between input and output, change over time causing the model's predicition to degrade.
- Monitoring would be achieved through **Sample Ground Truth** where new small batch images would be labeled periodically, and re-train the model when drift is detected.
3. Describe 1 technical challenge during deployment (e.g., scalability).
- *Data Privacy and Security*: Crop disease images may contain sensitive farm information or geolocation data of the farmer. Thus, before depolyment, relevant data protection regulations should be put into consideration.
- *Limited On-Device Resources*: Many farmers use low-end smartphones with limited memory. Thus, lightweight models and cloud processing would be a best choice.

## Part 2: Case Study Application (40 points)

Scenario: A hospital wants an AI system to predict patient readmission risk within 30 days of discharge.

Tasks:

### Problem Scope (5 points): Define the problem, objectives, and stakeholders.

### Data Strategy (10 points):

 Propose data sources (e.g., EHRs, demographics).

 Identify 2 ethical concerns (e.g., patient privacy).

 Design a preprocessing pipeline (include feature engineering steps).

### Model Development (10 points):

Select a model and justify it.

Create a confusion matrix and calculate precision/recall (hypothetical data).

### Deployment (10 points):

Outline steps to integrate the model into the hospital’s system.

How would you ensure compliance with healthcare regulations (e.g., HIPAA)?

Optimization (5 points): Propose 1 method to address overfitting.

## Part 3: Critical Thinking (20 points)

### Ethics & Bias (10 points):

How might biased training data affect patient outcomes in the case study?

Suggest 1 strategy to mitigate this bias.

### Trade-offs (10 points):

Discuss the trade-off between model interpretability and accuracy in healthcare.

If the hospital has limited computational resources, how might this impact model choice?

## Part 4: Reflection & Workflow Diagram (10 points)

### Reflection (5 points):

What was the most challenging part of the workflow? Why?

How would you improve your approach with more time/resources?

### Diagram (5 points):

Sketch a flowchart of the AI Development Workflow, labeling all stages.