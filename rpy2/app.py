from rpy2.robjects import r

def lambda_handler(event, context):
   number = event['number']
   r('''source("utils.R")''')
   return r['parity'](number)[0]
