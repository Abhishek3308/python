emp={'Antony':55000,'Susan':45000,'Kiran':60000}
result={name:'high' if x>50000 else 'low' for name,x in emp.items()}
print(result)
