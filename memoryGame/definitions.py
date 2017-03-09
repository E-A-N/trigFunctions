trig={}

functions = {
    "sine": {
        "name":"sine",
        "reciprical": "secant",
        "formula": "opposite / hypotenuse or y/r",
        "definition": "function for the ratio of the opposite side of a given angle over hypotenuse",
    },
    "cosine": {
        "name":"cosine",
        "reciprical": "cosecant",
        "formula": "adjacent / hypotenuse or x/r",
        "definition": "function for the ratio of adjacent side of a given angle over hypotenuse",
    },
    "tangent": {
        "name":"tangent",
        "reciprical": "cotangent",
        "formula": "opposite / adjacent or y/x",
        "definition": "function for the adjacent end of a given angle over hypotenuse",
    },
    "secant": {
        "name":"secant",
        "reciprical": "sine",
        "formula": "hypotenuse / opposite or r/y",
        "definition": "A function for the adjacent end of a give angle over hypotenuse",
    },
    "cosecant": {
        "name":"cosecant",
        "reciprical": "cosign",
        "formula": "hypotenuse / adjacent or r/x",
        "definition": "A function for the adjacent end of a given angle over hypotenuse"
    },
    "cotangent": {
        "name":"cotangent",
        "reciprical": "tangent",
        "formula": "adjacent / opposite or x/y",
        "definition": "A function for the ratio of the adjacent side a given angle over the hypotenuse",
    },
}

triangle = {
    "hypotenuse": {
        "name":"hypotenuse",
        "formula": "The square root of adjacent squared plus opposite squared or (x^2 + y^2)^0.5",
        "definition": "The opposite side that is the longest side the right angle in a right triangle. Referred to as 'r'",
    },
    "opposite": {
        "name":"hypotenuse",
        "formula": "(x^2 + y^2)^0.5",
        "definition": "The Longest side of a right triangle, opposite of the right angle.  Often referred to as the variable 'x'",
    },
}
angles = {
    "complement": {
        "name":"Complement",
        "definition": "The difference of two angles angles whose sume is 90 degrees"
    },
    "supplement": {
        "name":"Supplement",
        "definition": "The difference of two angles whose sum is 180 degrees"
    },
    "degrees": {
        "name":"Degrees",
        "definition": "A unit used to measure an angle"
    },
    "minutes": {
        "name":"Minutes",
        "definition": "A unit for measuring angles more precise than degree units, 60 minutes is equal to 1 degrees"
    },
    "theta": {
        "name":"Theta",
        "definition": "A unit for measuring angles more precise than degree units, 60 minutes is equal to 1 degrees"
    },
}

trig["functions"] = functions
trig["triangle"] = triangle
trig["angles"] = angles
