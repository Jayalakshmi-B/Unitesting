#importing required packages
import json

#Creating lambda handler function
def lambda_handler(event, ):
    print(event)
    numbers = event['numbers']
    response = json.dumps({"Armstrong":armstrong(numbers[0],numbers[1])})  #converting python to json
    return {
        "statusCode": 200,
        "body": response,
    }

#Creating Armstrong Function
def armstrong(numbers,sum):
    try:
        temp = numbers
        if numbers == 0:
            return "No Zero"
        else:
            while temp > 0:
                k = temp % 10
                sum += k * k * k
                temp = temp // 10

            if sum == numbers:
                return "Passed"
            else:
                raise ValueError
#throws error when the given number is not an armstrong
    except ValueError:
        return "Error"
