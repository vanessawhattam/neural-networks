[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/rEyuOVhC)
# Neural Network THA
To submit, please perform the following:
1. Save a script file for Python with the following name: `tha_lastname_firstname.py` where lastname is your last name and firstname is your first name.
1. Answer questions in `submission.md`.
1. Create screenshots and save to the directory `assets`.
1. Link the images of your screenshots from `assets` to `submission.md` where appropriate.
1. Push your assignment to GitHub.

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

For your model, create new columns in your data for lag effects of 2-periods, 3-periods, and 5-periods. (3 pts.)
* Create training and testing data. (2 pts.)
* For your model, create three ANN models and compare the error scores. (3 pts.)
* Which ones perform better and why? (2 pts.)

