# Shopping-Cart-Exercise

![image](https://user-images.githubusercontent.com/59658326/79157091-f57c6b80-7da1-11ea-92c0-fad8185bff36.png)

## Description

This repository is able to create a grocery store receipt from a list of products! The final receipt will list all the products purhcased, date & time, subtotal, tax amount, total amount and store location. This repo has also been configured to email your receipt.  

## Installation

Fork this repository and clone (or dowload) the repo onto your desktop. You can use GitHub Desktop or your command line to clone the repo. 

Navigate to the repo from the command line. For example:

```sh
cd /c/Users/name/Desktop/shopping-cart/
```

Use the command line or Visual Studio Code to create a file called shopping_cart.py 

## Set Up: Shopping Environment (1 time only)

Create and activate a shopping environment:
```sh
conda create -n shopping-env python=3.7
conda activate shopping-env
```
Install pandas, pytest, and dotenv
```sh
pip install pandas
pip install pytest
pip install python=dotenv
```

## Set Up: Custom Tax Rate

Create an .env file in the root directory.

Store your custom tax rate as an environment variable in the .env file.

```sh
TAX_RATE = .0875
```

## Usage

Run shopping_cart.py and print products to make sure it works!
```sh
python app/shopping_cart.py
```

You can test your changes by running pytest from the command line
```sh
pytest
```

## Final Output
Your Final output should look similar to the output below. 

![Finaloutput](https://user-images.githubusercontent.com/59658326/74206823-0ba76780-4c4b-11ea-93c5-10b0020e38cf.JPG)

### Best of luck and have fun!

