
# Neural Network THA

## Networking for healthcare
Proud of your achievements on the last project, Randall Cunningham would like to see the financial data modeled in a neural network. Use the [calihospital_financial.txt](/data/calihospital_financial.txt) time-ordered data.

Below is the data dictionary. Please use the variable `GROP_TOT` for this assignment.

| Item | Definition |
|:---|:---|
| QRT | The date of the entry in the format of year-q# where *year* is 4 digits and *q#* is the quarter in the year |
| GRIP_TOT | Gross inpatient revenue, total |
| GROP_TOT | Gross outpatient revenue, total |
| NET_TOT | Total net patient revenue |
| TOT_OP_EXP | Total operating expenses |
| NONOP_REV | Nonoperating revenue net of nonoperating expenses |

In the instructions I ask you to propose an ARIMA model. Since we did not cover time series, I do not expect you to do this. Here are the adjusted  instructions:
He requests you perform the following tasks:

* For your model, create three ANN models and compare the error scores. (3 pts.)
For this model, I created two models that used a 'relu' activation and one that used a 'logistic' activation. One 'relu' and the 'logistic' model both used the lag2 and lag5 columns, while the second 'relu' model used all 3 lag columns. The model with the lowest MAE and MSE was the 'logistic' model, titled `grop_ann2`. `grop_ann1` and `grop_ann3` performed similarly poorly on the measures of MAE and MSE, with scores of 3.6e+33 & 1.3e+67 and 1.1e+34 and 1.2e+68. These values are very far from the actual value. 

* Which ones perform better and why? (2 pts.)
The model that performs the best is the second model. The logistic model seems to match the data the best, although the error is still very large. Further, this model uses fewer variables so it can be easily run. Smaller errors are preferred because that means that the predictions more closely match the actual values, indicating that the predictions are more accurate. 