echo "####    POPULATING USERS ...    ####"
echo ""


curl --request POST \
    --verbose --include \
    --header 'Content-Type: application/json' 'Accept: application/json' \
    --data '
        {
            "userid": 1,
            "username": "Adam",
            "email": "adam@gmail.com",
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
            "email": "jennifer@gmail.com",
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
            "email": "jason@gmail.com",
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
            "email": "hannah@gmail.com",
            "karma": 1
        }' \
    http://127.0.0.1:6500/api/v2/user/create


echo ""
echo "####    4 USERS CREATED SUCCESSFULLY!!    ####"
