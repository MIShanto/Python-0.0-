#list
a = [1,2,3,4,5,6,7,8,9,10]

even = [i for i in a if i%2==0]
odd = set(a)
odd = {i for i in odd if i%2!=0}
print(odd)
print(even)

#dict
city = ["a","c","e","g"]
country = ["b","d","f", "h"]

tup = zip(city, country)
out = {city:country for city, country in tup}
print(out)