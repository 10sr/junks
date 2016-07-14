println "this is groovy script!"
println("this also prints a string")


// list
aList = ["elem1", "elem2"]

println aList
// puts [elem1, elem2]

aList << "elem3"

println aList
// puts [elem1, elem2, elem3]


a = [
    "name": "value",
    "name2": "value2"
]

println a.name
println a.name3
println a["name3"]
