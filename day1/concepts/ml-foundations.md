# Machine Learning Foundations

Reference for the core ideas behind machine learning: how it differs from rule-based code, the two main families of learning, and how to build and evaluate a model.

---

## Rule-Based Code vs Machine Learning

Rule-based programming needs a person to write every rule by hand. Machine learning shows a model many examples and lets it infer the rules from data.

Reach for machine learning when the rules are hard to state by hand, when patterns change over time, or when you have data that pairs inputs with the outcome you care about. Plain code is still the better choice when the logic is simple, fixed, and easy to write down.

## What a Model Is

A trained model is a mathematical function. It takes input data (features), returns a prediction, and bases that prediction on patterns learned during training. Training is the process that turns data into those learned patterns.

## Supervised vs Unsupervised Learning

| Family | Data | Goal | Examples |
| :--- | :--- | :--- | :--- |
| **Supervised** | Labeled | Map inputs to known answers | Classification, regression |
| **Unsupervised** | Unlabeled | Find structure | Clustering, dimensionality reduction |

Supervised learning splits into classification (predict a category) and regression (predict a number). Unsupervised learning is useful when labels are expensive or you are exploring the data.

## The ML Workflow

1. **Frame the problem:** decide what you are predicting and how success is measured.
2. **Collect and clean data:** handle missing values, remove errors.
3. **Feature engineering:** turn raw data into signals the model can use.
4. **Train the model:** fit it on the training set.
5. **Evaluate:** score it on held-out data.
6. **Deploy and monitor:** ship it, then watch for drift.

Real projects loop back from evaluation to earlier steps many times.

## Train, Validation, and Test Splits

Split the data so the model is scored on examples it never trained on:

- **Training set** (~70%): the model learns here.
- **Validation set** (~15%): tune settings and compare models here.
- **Test set** (~15%): the final, honest estimate of real-world performance.

Scoring a model on its own training data gives a falsely high number.

## Overfitting and Underfitting

- **Underfitting:** the model is too simple, so error is high on both training and test data.
- **Overfitting:** the model memorizes noise, so training error is low but test error is high.
- **Good fit:** error is low on both, and the model generalizes to new data.

A large gap between training and test scores is the classic sign of overfitting. Common fixes include more data, simpler models, and regularization.

## Evaluation Metrics

| Metric | Answers | Note |
| :--- | :--- | :--- |
| **Accuracy** | Fraction predicted correctly | Misleading on imbalanced data |
| **Precision** | Of predicted positives, how many were right | |
| **Recall** | Of actual positives, how many were found | |
| **F1** | Harmonic mean of precision and recall | Good single summary |

Choose metrics that match the problem. On a rare-disease test, recall usually matters more than raw accuracy.
