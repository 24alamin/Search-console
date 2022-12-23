import searchconsole
account = searchconsole.authenticate(client_config='client_secrets.json')
webproperty = account['https://www.allplace.xyz/']
report = webproperty.query.range('today', days=-14).dimension('query').get()
print(report.rows)