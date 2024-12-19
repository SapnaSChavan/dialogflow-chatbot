from flask import Flask, request,jsonify
from forex_python.converter import CurrencyRates


app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency'][0]['currency']
    amount =  data['queryResult']['parameters']['unit-currency'][0]['amount']
    target_currency =  data['queryResult']['parameters']['currency-name'][0]
    print(amount)
    print(source_currency)
    print(target_currency)
    cf = getConversionFactor(source_currency,target_currency)
    if cf !=0:
        finalAmount = amount*cf
        print(finalAmount)
        response = {
            'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,finalAmount,target_currency)
        }
    else:
        finalAmount = amount*cf
        print(finalAmount)
        response = {
            'fulfillmentText':"Conversion from {} to {} is not supported. ".format(source_currency,target_currency)
        }
    return jsonify(response)

def getConversionFactor(source,target):
     # Define a nested dictionary to store conversion rates
    conversion_rates = {
        "USD": {"EUR": 0.88, "INR": 70.5, "GBP": 0.74},
        "EUR": {"USD": 1.14, "INR": 80.0, "GBP": 0.85},
        "INR": {"USD": 0.014, "EUR": 0.0125, "GBP": 0.0105},
        "GBP": {"USD": 1.35, "EUR": 1.18, "INR": 95.0}
    }
    
    # Check if the source currency exists in the dictionary
    if source in conversion_rates:
        # Check if the target currency exists for the given source currency
        if target in conversion_rates[source]:
            return conversion_rates[source][target]
        else:
            return 0
    else:
        return 0

if __name__== "__main__":
    app.run(debug=True)