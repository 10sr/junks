#!/usr/bin/env groovy

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


b = [
    "hoge",
    "fuga"
]

println b
println b.join("\n")

println (
    [
        "fuag",
        "hlehle"
    ].join("\n")
)


println """${b}
"""

println """hoge"\${b}"
"""

String hoehoe = null

println hoehoe
try {
    Objects.requireNonNull(hoehoe);
} catch (e) {
    println e
}
