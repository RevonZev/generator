# random-traits-generator
A generator that generates from a json or json5 list dictionary

---

This generator can use JSON or JSON5.
```JSON
{
    "Main Trait": [
        "Claws",
        "Wings",
    ],
    "Claws made of if Main Trait is Claws": [
        "Iron",
        "Steel",
        "Keratin"
    ],
    "Wings made of if Main Trait is Wings": [
        "Feather",
        "Leather"
    ],
    "Chicken if Wings made of is Feather": [
        "Yes"
    ],
    "Satisfied": [
        "Yes",
        "No"
    ]
}
```