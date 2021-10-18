from typing import Dict, List, Tuple

#Example 1
positives: List[int] = [1, 2, 3, 4, 5]

#Example 2
users: Dict[str, int] = {
    'Argentina': 1,
    'Holanda': 15,
    'Peru': 100,
}

#Example 3
countries: List[Dict[str, str]] = [
    {
        'name': 'Peru',
        'people': '10235',
    },
    {
        'name': 'Holanda',
        'people': '505168',
    },
    {
        'name': 'Argentina',
        'people': '15569',
    }
]

#Example 4
numbers: Tuple[int, float, int] = (1, .5, 3)

#Example 5
CoordinatesType = List[Dict[str, Tuple[int, int]]] #Declarando como un objeto se puede!!

coorde: CoordinatesType = [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 5)
    },
]