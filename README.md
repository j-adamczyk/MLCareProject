# MLCare Project

This project is the software for my bachelor (Engineer of Computer Science in Poland) thesis "The system supporting preventive care and medical diagnosis using machine learning". It was done in collaboration with Magdalena Kozub and Natalia Organek. The thesis can be found in the PDF file.

## My work

I have been responsible for ML side. The main requirements for choosing the methods were:
- ability to cope with missing data during work
- high scalability
- explainability

## ML tech stack

- Python
- Numpy
- Pandas
- Matplotlib
- Scikit-learn
- Scikit-optimize
- XGBoost
- SHAP

## ML approach

I chose XGBoost as the main prediction algorithm, since it effectively uses the missing attributes (the split calculation creates the additional "default" direction for missing values) and is highly scalable. It can also output the probability of predicted class, which increases interpretability of results.

For hyperparameter optimization I've used Gaussian process regression, since this method is available as a plug-in in Scikit-optimize and is fast for multiple attributes, also being more "intelligent" search of the hyperparameter space than random search.

Explainability of predictions is provided with force plots from the SHAP library. It has efficient implementation for tree-based classifiers and also allows for missing values (unlike LIME). It works well with Pandas library, plotting feature names and their individual impact on prediction.

## Datasets

For the proof-of-concept, I used 3 datasets from UCI:
- [Acute Inflammations](https://archive.ics.uci.edu/ml/datasets/Acute+Inflammations)
- [Breast Cancer Coimbra](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra)
- [Breast Cancer Wisconsin](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))

Application can be easily extended to use other datasets. The modular construction of the input data minimizes the work required to do so - it just needs a function to load the data in the required format.

## Sample images
![chrome_y4wg92Ihwq](https://user-images.githubusercontent.com/50807718/110822394-4dad3d80-8291-11eb-8fae-9c3d3ee06a3d.png)
![chrome_q0xtkVYpkY](https://user-images.githubusercontent.com/50807718/110822409-51d95b00-8291-11eb-800a-9a8db5e1fb8b.png)
![chrome_kUBwqcutXb](https://user-images.githubusercontent.com/50807718/110822416-543bb500-8291-11eb-86cd-1011a00edc7d.png)
![chrome_rWZ74nvvIJ](https://user-images.githubusercontent.com/50807718/110822421-556ce200-8291-11eb-9242-b89048115afb.png)
![chrome_K3eqGSSEFB](https://user-images.githubusercontent.com/50807718/110822429-569e0f00-8291-11eb-88f6-a7d53711672d.png)


## Setup
To run application:
```
cd backend

flask run

cd frontent npm start
```
App runs on port `localhost:4200`
