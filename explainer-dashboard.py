from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split


# import necessary libraries and load the dataset
from sklearn.linear_model import LinearRegression


from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import RegressionExplainer, ClassifierExplainer, ExplainerDashboard, ExplainerHub
import pandas as pd



if __name__ == "__main__":
    # Breast Cancer
    # Load the Breast Cancer Wisconsin (Diagnostic) dataset
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='target')


    model = RandomForestClassifier(n_estimators=50, max_depth=5)
    model.fit(X, y)

    explainer = ClassifierExplainer(model, X, y, cats=[0], labels=['Benign', 'Malignant'])


    db1 = ExplainerDashboard(explainer, 
                            title="Breast Cancer Explainer", # defaults to "Model Explainer"
                            shap_interaction=True, # you can switch off tabs with bools
                            )


    # Load the diabetes dataset
    diabetes = load_diabetes()
    X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    y = pd.Series(diabetes.target, name = 'target')

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a machine learning model on the training set
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Use the ExplainerDashboard library to create an interactive dashboard
    explainer = RegressionExplainer(model, X_test, y_test)
    db2 = ExplainerDashboard(explainer, 
                            title="Diabetes Explainer", # defaults to "Model Explainer"
                            shap_interation=True)

    hub = ExplainerHub([db1, db2])
    hub.run()
