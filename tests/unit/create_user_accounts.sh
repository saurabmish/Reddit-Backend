curl --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "name": "Adam",
            "location": "New York",
            "gender": "M"
        }' \
    http://127.0.0.1:6500/api/v1/user/create


curl --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "name": "Jennifer",
            "location": "Anaheim",
            "gender": "F"
        }' \
    http://127.0.0.1:6500/api/v1/user/create


curl --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "name": "Jason",
            "location": "Mission Viejo",
            "gender": "M"
        }' \
    http://127.0.0.1:6500/api/v1/user/create


curl --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "name": "Hannah",
            "location": "Fullerton",
            "gender": "F"
        }' \
    http://127.0.0.1:6500/api/v1/user/create