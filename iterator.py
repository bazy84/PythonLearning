#iteration protocol

iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) #produces a StopIteration exception
