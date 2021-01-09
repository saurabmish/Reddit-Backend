echo "####    POPULATING USERS ...    ####"
echo ""


curl --request POST \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "userid": 1,
            "username": "Adam",
            "email": "New York",
            "karma": 1
        }' \
    http://127.0.0.1:6500/api/v2/user/create


curl --request POST \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "userid": 2,
            "username": "Jennifer",
            "email": "Anaheim",
            "karma": 1
        }' \
    http://127.0.0.1:6500/api/v2/user/create


curl --request POST \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "userid": 3,
            "username": "Jason",
            "email": "Mission Viejo",
            "karma": 1
        }' \
    http://127.0.0.1:6500/api/v2/user/create


curl --request POST \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "userid": 4,
            "username": "Hannah",
            "email": "Fullerton",
            "karma": 1
        }' \
    http://127.0.0.1:6500/api/v2/user/create


echo ""
echo "####    4 USERS CREATED SUCCESSFULLY!!    ####"
