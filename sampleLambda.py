def lambda_handler(event, context):
    value1 = event['value1']
    value2 = event['value2']
    if (value1 % 2) == 0:
        console.log("{0} is Even".format(value1))
    else:
        console.log("{0} is Odd".format(value1))
    sum = value1 + value2
    product = value1 * value2
    diff = value1 - value2
    quotient = value1 / value2
    return {
       "Value1": value1,
       "Value2": value2,
       "Sum": sum,
       "Product": product,
       "Difference": diff,
       "Quotient": quotient
    }